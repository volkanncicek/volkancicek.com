from datetime import datetime

AUTHOR = "Volkan Çiçek"
SITENAME = "Volkan Çiçek"
SITEURL = ""
SITE_DESCRIPTION = (
    "Senior Data Scientist & AI Engineer specializing in Generative AI, LLMs, and MLOps"
)

PATH = "content"
OUTPUT_PATH = "output/"
THEME = "./theme"

# Content paths
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["posts"]

TIMEZONE = "Europe/Istanbul"
DEFAULT_LANG = "en"
CURRENT_YEAR = datetime.now().year

# Contact
EMAIL = "volkanciicek@gmail.com"

# Intro text for homepage
INTRO_TEXT = "Senior Data Scientist & AI Engineer with a Mathematics background. I work at the intersection of Generative AI, LLMs, RAG systems, and MLOps — turning complex AI ideas into production-ready solutions."

# Static files (CV, etc.)
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/cv.pdf": {"path": "cv.pdf"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extra/og-image.png": {"path": "og-image.png"},
}

# Projects - Projelerinizi buraya ekleyin
PROJECTS = (
    {
        "name": "PyData Archive",
        "description": "An archive of PyData conference talks and tutorials. PyData is an educational program of NumFOCUS that provides a forum for the international community of users and developers of data analysis tools.",
        "url": "https://pydataarchive.com",
        "status": "active",
    },
    {
        "name": "Voice Dub Studio",
        "description": "AI-powered voice dubbing and translation platform for video content.",
        "url": "https://voicedubstudio.com",
        "status": "active",
    },
    {
        "name": "Alcatel Modem API",
        "description": "Generic Python library and CLI tool for Alcatel LTE modems. Supports multiple Alcatel models with SMS management, network monitoring, and API access.",
        "url": "https://github.com/volkanncicek/alcatel-modem-api",
        "status": "active",
    },
    {
        "name": "Input Lock",
        "description": "A desktop app that temporarily locks your keyboard and mouse input. Perfect for cleaning breaks or preventing accidental input.",
        "url": "https://github.com/volkanncicek/input-lock",
        "status": "active",
    },
)

# URL settings — extensionless URLs, .html save paths (Cloudflare Pages serves both)
# Internal links / canonical / sitemap use the URL form that returns 200 directly,
# avoiding the 308 redirect Cloudflare Pages applies to *.html requests.
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}.html"
PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}.html"

# Per-item taxonomy pages disabled — with a small post count they are thin/duplicate
# content that Google won't index. Re-enable once each tag/category has multiple
# substantial posts that warrant their own hub page.
CATEGORY_SAVE_AS = ""
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""

# Direct templates — archives kept as the single navigable index; categories/tags
# cloud pages dropped (they link to the now-disabled per-item pages).
DIRECT_TEMPLATES = ["index", "archives", "projects"]
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = "archives.html"
PROJECTS_URL = "projects"
PROJECTS_SAVE_AS = "projects.html"

# Custom template pages (örn. 404)
TEMPLATE_PAGES = {
    "404.html": "404.html",
}

# Menu settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = ()

# Feed generation (şimdilik kapalı)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget - Sosyal medya hesaplarınız
SOCIAL = (
    ("GitHub", "https://github.com/volkanncicek"),
    ("LinkedIn", "https://linkedin.com/in/volkanncicek"),
    ("Twitter", "https://twitter.com/volkanncicek"),
)

# Twitter username for meta tags (without @)
TWITTER_USERNAME = "volkanncicek"

# Open Graph locale (e.g. "en_US", "tr_TR")
OG_LOCALE = "en_US"

# Search engine verification — sadece content="..." kısmındaki string'i koy
# Google Search Console → Settings → Ownership verification → HTML tag
GOOGLE_SITE_VERIFICATION = ""
# Bing Webmaster Tools → Site → Verify Ownership → Meta tag (gerekirse)
BING_SITE_VERIFICATION = ""

# Sayfa başına makale sayısı
DEFAULT_PAGINATION = 10

# Summary settings
SUMMARY_MAX_LENGTH = 50

# Cache settings (development için kapalı)
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "neighbors", "series", "plugins.llms", "plugins.merlican"]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "plugins.merlican.mermaid_markdown": {},
    },
    "output_format": "html5",
}

# Typography enhancements (smart quotes, etc.)
TYPOGRIFY = True

# Analytics
GOAT_COUNTER = "volkancicek"

# Sitemap settings — keep only content URLs (homepage, about page, blog posts).
# Plugin matches `exclude` regex against path-relative URLs (no leading slash for
# direct templates) and against obj.url for articles/pages. Nav-only index pages
# (archives, projects) are reached via internal links from every page — they
# don't need to be in the sitemap.
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.8},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
    "exclude": [
        r"^404\.html$",
        r"^archives\.html$",
        r"^projects\.html$",
        r"^author/",
        r"^tag/",
        r"^category/",
    ],
}
