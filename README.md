# volkancicek.com

Personal website and blog built with [Pelican](https://getpelican.com/).

## Quick Start

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
# Create virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt
```

### Development

```bash
# Start development server with live reload
uv run pelican --listen --autoreload

# Or using invoke tasks
uv run invoke livereload
```

The site will be available at `http://localhost:8000`.

### Build

```bash
# Build the site
uv run pelican content

# Build for production
uv run pelican content -s publishconf.py
```

## Project Structure

```
volkancicek.com/
├── content/
│   ├── extra/          # Static files (robots.txt, cv.pdf, favicon.ico)
│   ├── images/         # Blog images
│   ├── pages/          # Static pages (about.md)
│   └── posts/          # Blog posts (*.md)
├── plugins/
│   └── llms/           # LLMs.txt generator plugin
├── theme/
│   ├── static/css/     # Stylesheets (with dark mode support)
│   └── templates/
│       ├── partials/   # Reusable template parts (head, nav, footer)
│       └── *.html      # Page templates
├── output/             # Generated site (git ignored)
├── pelicanconf.py      # Development config
├── publishconf.py      # Production config
└── requirements.txt    # Python dependencies
```

## Writing Content

### Blog Posts

Create a new `.md` file in `content/posts/`:

```markdown
Title: My Post Title
Date: 2026-01-27 10:00
Category: Blog
Tags: tag1, tag2
Slug: my-post-title

Your content here...
```

### Pages

Create a new `.md` file in `content/pages/`:

```markdown
Title: Page Title
Slug: page-slug

Your content here...
```

## Deployment

The site is hosted on **Cloudflare Pages** with a custom domain.

### Build Settings (Cloudflare Pages)

| Setting | Value |
|---------|-------|
| Build command | `pelican content -s publishconf.py` |
| Build output directory | `output` |
| Root directory | `/` |

### Manual Build

```bash
# Build for production
uv run pelican content -s publishconf.py
```

Push to your connected Git repository and Cloudflare Pages will automatically build and deploy.

## License

Content © Volkan Çiçek. All rights reserved.
