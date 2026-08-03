"""
LLMs.txt Generator Plugin for Pelican

Generates a llms.txt file that provides an AI-readable summary of site content.
This helps LLMs and AI agents better understand and index your website.
"""

import html
import re
from datetime import datetime
from pathlib import Path

from markdownify import ATX
from markdownify import markdownify as md
from pelican import contents, signals

_HTML_TAG = re.compile(r"<[^>]+>")
_TRAILING_SPACE = re.compile(r"[ \t]+\n")
_BLANK_RUN = re.compile(r"\n{3,}")
_LEADING_HEADING = re.compile(r"\A#\s+.*?\n+")
_HEADING_LINE = re.compile(r"^#{1,5}(?= )", re.MULTILINE)


def _plain_text(value) -> str:
    """Reduce a rendered title to plain text.

    Titles reach this plugin after TYPOGRIFY has run, so they carry markup the rest
    of the site wants but this file does not: `<span class="caps">NVIDIA</span>`,
    `&nbsp;`, `&#8217;`. llms.txt exists to hand crawlers clean text, so strip the
    tags and decode the entities.
    """
    return html.unescape(_HTML_TAG.sub("", str(value))).strip()


class LLMSGenerator:
    """Generator class for creating llms.txt file."""

    def __init__(self, context, settings, path, theme, output_path, *args, **kwargs):
        self.context = context
        self.settings = settings
        self.output_path = Path(output_path)
        self.siteurl = settings.get("SITEURL", "")
        self.sitename = settings.get("SITENAME", "My Site")
        self.site_description = settings.get("SITE_DESCRIPTION", "")
        self.now = datetime.now()

    def generate_output(self, writer):
        """Generate the llms.txt output file."""
        about_content = self._get_about_summary()
        pages = self.context.get("pages", [])
        articles = self.context.get("articles", [])

        lines = [f"# {self.sitename}", ""]
        lines.append(f"> {self.site_description}")
        lines.append("")

        if about_content:
            lines.append("## About")
            lines.append(about_content)
            lines.append("")

        # About is rendered in full above, so it is not repeated here. Filter first:
        # testing `pages` instead left an empty "## Pages" heading behind.
        other_pages = [p for p in pages if p.slug != "about"]
        if other_pages:
            lines.append("## Pages")
            for page in other_pages:
                lines.append(self._format_entry(page))
            lines.append("")

        if articles:
            lines.append("## Blog Posts")
            for article in articles:
                lines.append(self._format_entry(article))
            lines.append("")

        # Add generation timestamp
        lines.append("---")
        lines.append(f"Generated: {self.now.strftime('%Y-%m-%d')}")
        lines.append(f"Source: {self.siteurl}")

        llms_txt_path = self.output_path / "llms.txt"
        llms_txt_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[llms_txt] Wrote {llms_txt_path}")

    def _get_about_summary(self) -> str:
        """Extract content from the about page."""
        about_page = next(
            (p for p in self.context.get("pages", []) if p.slug == "about"), None
        )
        if not about_page:
            return ""

        # ATX headings (`## X`) rather than markdownify's underlined default, which
        # renders as a bare `========` line once the surrounding structure is gone.
        content = md(about_page.content, heading_style=ATX).strip()

        # Collapse only what is genuinely excess. Joining on whitespace, as this used
        # to, flattened the whole page into a single unreadable line.
        content = _TRAILING_SPACE.sub("\n", content)
        content = _BLANK_RUN.sub("\n\n", content)

        # The page opens with its own "About Me" H1, which would sit under the "##
        # About" heading this plugin already wrote.
        content = _LEADING_HEADING.sub("", content).strip()

        # Demote what is left by one level. The page's own H2s would otherwise rank
        # equal to this file's "## About" and "## Blog Posts", reading as site
        # sections rather than parts of the about page.
        return _HEADING_LINE.sub(r"#\g<0>", content)

    def _format_entry(self, item: contents.Content) -> str:
        """Format a page or article entry for the llms.txt file."""
        url = item.url.removesuffix("/")

        # Try description, then summary metadata
        description = (
            getattr(item, "description", None) or getattr(item, "summary", None) or ""
        )
        description = str(description).strip()

        # Strip HTML tags and convert to plain text
        description = md(description).strip().replace("\n", " ")
        description = _BLANK_RUN.sub(" ", description)

        title = _plain_text(item.title)

        # Handle external URLs (e.g., starting with http)
        if url.startswith("http"):
            link = f"- [{title}]({url})"
        else:
            link = f"- [{title}]({self.siteurl}/{url})"

        if description:
            return f"{link}: {description}"
        return link


def get_generators(_):
    """Return the LLMSGenerator class."""
    return LLMSGenerator


def register():
    """Register the plugin with Pelican."""
    signals.get_generators.connect(get_generators)
