import logging

from pelican import signals

log = logging.getLogger(__name__)

# Pinned so a compromised or breaking upstream release cannot reach readers, and
# guarded with a subresource integrity hash so the CDN cannot serve anything else.
# To upgrade: bump the version, fetch the file, and recompute the hash with
#   openssl dgst -sha384 -binary mermaid.min.js | openssl base64 -A
MERMAID_VERSION = "11.16.0"
MERMAID_SRI = "sha384-T/0lMUdJpd2S1ZHtRiofG3htU3xPCrFVeAQ1UUE2TJwlEJSV5NUwn30kP28n238E"

MARKER = '<pre class="mermaid">'
CLOSING_BODY = "</body>"


def register():
    signals.content_written.connect(add_mermaid_script)


# Not deferred, matching the loading behaviour this plugin has always had. The tags
# sit just before </body> so they do not block first render anyway, and `defer` was
# measured without producing a reproducible improvement. Whatever is done here is
# marginal next to the real cost: the bundle is ~930 KB over the wire and Lighthouse
# reports ~806 KB of it as unused. Cutting that means rendering diagrams to SVG at
# build time instead of shipping mermaid to readers.
def _script_tags(siteurl):
    return (
        f'<script src="https://cdn.jsdelivr.net/npm/mermaid@{MERMAID_VERSION}/dist/mermaid.min.js"'
        f' integrity="{MERMAID_SRI}" crossorigin="anonymous"></script>\n'
        f'<script src="{siteurl}/theme/js/mermaid-init.js"></script>\n'
    )


def add_mermaid_script(path, context):
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()

        if MARKER not in content or "mermaid.min.js" in content:
            return

        tags = _script_tags(context.get("SITEURL", ""))
        if CLOSING_BODY in content:
            content = content.replace(CLOSING_BODY, tags + CLOSING_BODY, 1)
        else:
            # No body element to anchor to (unexpected for this theme); append rather
            # than silently dropping the diagrams.
            content += "\n" + tags
            log.warning("[Merlican] No %s in %s, appended instead", CLOSING_BODY, path)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        log.warning("[Merlican] Error injecting Mermaid script into %s: %s", path, e)
