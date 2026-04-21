import logging
from pelican import signals

log = logging.getLogger(__name__)

MERMAID_SCRIPT = (
    '<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>\n'
    '<script>mermaid.initialize({startOnLoad:true});</script>'
)


def register():
    signals.content_written.connect(add_mermaid_script)


def add_mermaid_script(path, context):
    try:
        with open(path, "r+", encoding="utf-8") as f:
            content = f.read()
            if '<pre class="mermaid">' in content and "mermaid.min.js" not in content:
                f.seek(0, 2)
                f.write("\n" + MERMAID_SCRIPT)
    except Exception as e:
        log.warning("[Merlican] Error injecting Mermaid script into %s: %s", path, e)
