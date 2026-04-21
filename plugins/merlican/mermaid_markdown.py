import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class MermaidBlockPreprocessor(Preprocessor):
    # Using <pre> so TYPOGRIFY skips the content (avoids -- -> em-dash conversion)
    RE = re.compile(r"^```mermaid\s*\n([\s\S]+?)^```", re.MULTILINE)

    def run(self, lines):
        text = "\n".join(lines)

        def repl(match):
            code = match.group(1).rstrip()
            return f'<pre class="mermaid">{code}</pre>'

        text = self.RE.sub(repl, text)
        return text.splitlines()


class MermaidExtension(Extension):
    def extendMarkdown(self, md):
        # Priority 50 ensures this runs before fenced_code (25) and grabs ```mermaid first
        md.preprocessors.register(MermaidBlockPreprocessor(md), "mermaid_block", 50)


def makeExtension(**kwargs):
    return MermaidExtension(**kwargs)
