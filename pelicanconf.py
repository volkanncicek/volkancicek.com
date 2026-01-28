from datetime import datetime

AUTHOR = "Volkan Çiçek"
SITENAME = "Volkan Çiçek"
SITEURL = ""
SITE_DESCRIPTION = (
    "Senior Data Scientist specializing in Generative AI, LLMs, and MLOps"
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
INTRO_TEXT = "Senior Data Scientist with a Mathematics background. I work at the intersection of Generative AI, LLMs, RAG systems, and MLOps — turning complex AI ideas into production-ready solutions."

# Static files (CV, etc.)
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/cv.pdf": {"path": "cv.pdf"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
}

# Manifesto - Ana sayfada görünecek kişisel manifesto (şimdilik kapalı)
# Açmak için MANIFESTO değişkenini aktif edin
# MANIFESTO = """
# I believe in building things that matter. Technology should empower people, not exploit them.
# I write code, break things, learn from failures, and share what I discover along the way.
# This is my corner of the internet — raw thoughts, projects, and experiments.
# """

# Projects - Projelerinizi buraya ekleyin
PROJECTS = (
    {
        "name": "PyData Archive",
        "description": "A curated archive of Python data science resources, tutorials, and best practices.",
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

# URL settings
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"

# Direct templates - projects sayfası için
DIRECT_TEMPLATES = ["index", "archives", "categories", "tags", "projects"]
PROJECTS_SAVE_AS = "projects.html"

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
PLUGINS = ["sitemap", "plugins.llms"]

# Typography enhancements (smart quotes, etc.)
TYPOGRIFY = True

# Sitemap settings
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.8},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}
