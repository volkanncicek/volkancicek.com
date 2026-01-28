"""
LLMs.txt Generator Plugin for Pelican

Generates a llms.txt file that provides an AI-readable summary of site content.
This helps LLMs and AI agents better understand and index your website.
"""

from datetime import datetime
from pathlib import Path

from markdownify import markdownify as md
from pelican import contents, signals


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

        if pages:
            lines.append("## Pages")
            for page in pages:
                if page.slug != "about":  # About is already included above
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
        
        content = md(about_page.content)
        # Clean up the content - remove excessive newlines
        content = " ".join(content.strip().split())
        return content

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

        # Handle external URLs (e.g., starting with http)
        if url.startswith("http"):
            link = f"- [{item.title}]({url})"
        else:
            link = f"- [{item.title}]({self.siteurl}/{url})"

        if description:
            return f"{link}: {description}"
        return link


def get_generators(_):
    """Return the LLMSGenerator class."""
    return LLMSGenerator


def register():
    """Register the plugin with Pelican."""
    signals.get_generators.connect(get_generators)
