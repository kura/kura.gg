#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Kura"
SITENAME = "kura.gg"
SITEURL = "https://kura.gg"
# SITEURL = 'https://kura.io'

THEME = "eevee"
THEME_PRIMARY = "deep_orange"
THEME_ACCENT = "red"
# THEME = 'eevee_original'
# THEME_PRIMARY = 'blue_grey'
# THEME_ACCENT = 'pink'
USE_TWITTER_CARDS = True
USE_OPEN_GRAPH = True

TIMEZONE = "Europe/London"

TWITTER_USERNAME = "kuramanga"
DISQUS_SITENAME = "syslogtv"

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = "en"

DEFAULT_DATE_FORMAT = "%d %b %Y"

DATE_FORMATS = {"en": DEFAULT_DATE_FORMAT}

HEADERID_LINK_CHAR = r"&#x203B;"
# HEADERID_LINK_CHAR = r'<i class="material-icons">&#xE8AB;</i>'

MENUITEMS = [
    (
        """<i class="material-icons" aria-hidden="true">&#xE871;</i> Eevee""",
        "Eevee",
        "/eevee/",
    ),
    (
        """<i class="material-icons" aria-hidden="true">&#xE0B7;</i> Contact""",
        "Contact",
        "/contact/",
    ),
    (
        """<i class="material-icons" aria-hidden="true">&#xE86F;</i> Software""",
        "Software",
        "/software/",
    ),
]

SOCIAL = [
    (
        """<i class="fa" aria-hidden="true">&#xF09B;</i> Github""",
        "GitHub",
        "https://github.com/kura",
    )
]

AUTHOR_CARD_SOCIAL = [
    (
        """<i class="fa" aria-hidden="true">&#xF09B;</i>""",
        "GitHub",
        "https://github.com/kura",
    )
]

LINKS = [
    (
        """<i class="material-icons" aria-hidden="true">&#xE86F;</i> Blackhole""",
        "Blackhole",
        "https://kura.gg/blackhole",
    ),
    (
        """<i class="material-icons" aria-hidden="true">&#xE86F;</i> Yarg""",
        "Yarg",
        "https://kura.gg/yarg",
    ),
    (
        """<i class="material-icons" aria-hidden="true">&#xE871;</i> Eevee""",
        "Eevee",
        "https://kura.gg/eevee",
    ),
    (
        """<i class="material-icons" aria-hidden="true">&#xE871;</i> Hauntr""",
        "Hauntr",
        "https://kura.gg/hauntr",
    ),
    (
        """<i class="material-icons" aria-hidden="true">&#xE871;</i> Ghastly""",
        "Ghastly",
        "https://kura.gg/ghastly",
    ),
]

DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"
AUTHOR_URL = "authors/{slug}/"
AUTHOR_SAVE_AS = "authors/{slug}/index.html"
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"
YEAR_ARCHIVE_SAVE_AS = "archives/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/index.html"

PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

SUMMARY_MAX_LENGTH = 150

STATIC_PATHS = [
    "images",
    "files",
    "extra/robots.txt",
    "extra/favicon.ico",
    "extra/favicon.png",
]

PAGE_EXCLUDES = ["files"]
ARTICLE_EXCLUDES = ["files"]

EXTRA_PATH_METADATA = {
    # "files": {"path": "files"},
    # "images": {"path": "images"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon.png": {"path": "favicon.png"},
    "extra/robots.txt": {"path": "robots.txt"},
}

DIRECT_TEMPLATES = ["404", "500", "archives", "categories", "index", "tags"]

TOC_HEADER = False

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "daily", "indexes": "daily", "pages": "daily"},
    # 'exclude': ['tag/', 'category/'],
}

FEED_ATOM = "feeds/atom.xml"
FEED_RSS = "feeds/rss.xml"
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_RSS = "feeds/all.rss.xml"
# CATEGORY_FEED_ATOM = 'feeds/category-%s.atom.xml'
# CATEGORY_FEED_RSS = 'feeds/category-%s.rss.xml'
# TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'
# TAG_FEED_RSS = 'feeds/tag-%s.rss.xml'
# AUTHOR_FEED_ATOM = 'feeds/author-%s.atom.xml'
# AUTHOR_FEED_RSS = 'feeds/author-%s.rss.xml'

PLUGIN_PATHS = ["plugins/"]
PLUGINS = [
    "assets",
    "better_tables",
    "extract_toc",
    "gallery",
    # "headerid",
    "lightbox",
    "neighbors",
    "pelican-ert",
    "pelican_fontawesome",
    "pelican_gist",
    "pelican_vimeo",
    "pelican_youtube",
    "related_posts",
    "series",
    "sitemap",
]

GIST_CACHE_ENABLED = False
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ["pre", "code", "meta", "title"]

MEGA_FOOTER = True

SEARCH_IGNORE = [
    "donate/" "tor/",
    "2016/06/12/eevee-a-material-design-theme-for-pelican/",
    "2014/06/09/hauntr/",
    "2014/05/26/ghastly-a-theme-for-pelican/",
    "2014/08/09/yarg/",
    "2014/06/08/pelican-fontawesome/",
    "2016/06/13/lightbox--a-pure-css-lightbox-for-pelican/",
]

DISCLAIMER = "Powered by love &amp; rainbow sparkles."
COPYRIGHT = (
    """Source code and content released under the <a href="/license/" """
    """title="MIT license">MIT license</a>."""
)

COMMENTS_ON_PAGES = True
USE_AUTHOR_CARD = True
AUTHOR_CARD_AVATAR = "/images/avatar.png"
AUTHOR_CARD_ON_PAGES = True
AUTHOR_CARD_DESCRIPTION = (
    "Anarchist. Pessimist. Bipolar. Hacker. Hyperpolyglot. Musician. Ex pro "
    "gamer. Cunt. They/Them."
)
