AUTHOR = 'Volkan Çiçek'
SITENAME = 'Volkan Çiçek'
SITEURL = ""
SITE_DESCRIPTION = "Senior Data Scientist specializing in Generative AI, LLMs, and MLOps"

PATH = "content"
OUTPUT_PATH = "output/"
THEME = "./theme"

# Content paths
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['']

TIMEZONE = 'Europe/Istanbul'
DEFAULT_LANG = 'en'
CURRENT_YEAR = 2026

# Contact
EMAIL = "volkanciicek@gmail.com"

# Intro text for homepage
INTRO_TEXT = "Senior Data Scientist with a Mathematics background. I work at the intersection of Generative AI, LLMs, RAG systems, and MLOps — turning complex AI ideas into production-ready solutions."

# Static files (CV, etc.)
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/cv.pdf': {'path': 'cv.pdf'},
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
        "name": "Project Alpha",
        "description": "A brief description of what this project does",
        "url": "https://github.com/volkancicek/project-alpha",
        "status": "active",  # active, completed, archived
    },
    {
        "name": "Project Beta",
        "description": "Another cool project you're working on",
        "url": "https://github.com/volkancicek/project-beta",
        "status": "completed",
    },
    # Daha fazla proje ekleyin...
)

# URL settings
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Direct templates - projects sayfası için
DIRECT_TEMPLATES = ['index', 'archives', 'categories', 'tags', 'projects']
PROJECTS_SAVE_AS = 'projects.html'

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

# Sayfa başına makale sayısı
DEFAULT_PAGINATION = 10

# Summary settings
SUMMARY_MAX_LENGTH = 50

# Cache settings (development için kapalı)
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
