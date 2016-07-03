#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kura'
SITENAME = 'kura.io'
SITEURL = 'https://kura.io'

THEME = 'eevee'
THEME_PRIMARY = 'deep_orange'
THEME_ACCENT = 'red'
USE_TWITTER_CARDS = True
USE_OPEN_GRAPH = True

TIMEZONE = 'Europe/London'

TWITTER_USERNAME = 'kuramanga'
DISQUS_SITENAME = "syslogtv"

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%d %b %Y'

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT
}

HEADERID_LINK_CHAR = '&para;'

MENUITEMS = (('<i class="material-icons">&#xE0B7;</i> Contact', '/contact/'),
             ('<i class="material-icons">&#xE86F;</i> Software', '/software/'),
             ('<i class="material-icons">&#xE02F;</i> Archives', '/archives/'),
             ('<i class="material-icons">&#xE263;</i> Donate', 'https://gratipay.com/~kura/'),
             ('<i class="material-icons">&#xE62F;</i> .onion', 'http://omgkuraio276g5wo.onion/'))
SOCIAL = (('<i class="fa fa-github aria-hidden="true"></i> Github', 'https://github.com/kura'),
          ('<i class="fa fa-twitter aria-hidden="true"></i> Twitter', 'https://twitter.com/kuramanga'),
          ('<i class="fa fa-key aria-hidden="true"></i> Keybase', 'https://keybase.io/kura'))
AUTHOR_CARD_SOCIAL = (('<i class="fa fa-github aria-hidden="true"></i>', 'https://github.com/kura'),
                      ('<i class="fa fa-twitter aria-hidden="true"></i>', 'https://twitter.com/kuramanga'),)
LINKS = (('<i class="material-icons">&#xE250;</i> blackhole.io', 'https://blackhole.io'),
         ('<i class="material-icons">&#xE250;</i> Yarg', 'https://kura.io/yarg'),
         ('<i class="material-icons">&#xE250;</i> Eevee', 'https://kura.io/eevee'),
         ('<i class="material-icons">&#xE250;</i> Hauntr', 'https://kura.io/hauntr'),
         ('<i class="material-icons">&#xE250;</i> Ghastly', 'https://kura.io/ghastly'),)
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

SUMMARY_MAX_LENGTH = 150

STATIC_PATHS = ['images', 'files', 'extra/robots.txt',
                'extra/favicon.ico', 'extra/favicon.png', ]

EXTRA_PATH_METADATA = {
    'files': {'path': 'files'},
    'images': {'path': 'images'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.png': {'path': 'favicon.png'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = ('index', 'archives', '404', 'tags', 'categories', 'search', )

TOC_HEADER = False

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily',
    },
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

PLUGIN_PATHS = ['plugins/', ]
PLUGINS = [
    'assets',
    'better_tables',
    'extract_toc',
    'headerid',
    'lightbox',
    'neighbors',
    'pelican_fontawesome',
    'pelican_gist',
    'pelican_vimeo',
    'pelican_youtube',
    'related_posts',
    'series',
    'sitemap',
    'touch',
]

GIST_CACHE_ENABLED = False
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ['pre', 'code', 'meta', 'title']

MEGA_FOOTER = True

SEARCH_IGNORE = [
    'donate/'
    'tor/',
    '2016/06/12/eevee-a-material-design-theme-for-pelican/',
    '2014/06/09/hauntr/',
    '2014/05/26/ghastly-a-theme-for-pelican/',
    '2014/08/09/yarg/',
    '2014/06/08/pelican-fontawesome/',
    '2016/06/13/lightbox--a-pure-css-lightbox-for-pelican/',
]

DISCLAIMER = 'Powered by love &amp; rainbow sparkles.'
COPYRIGHT = 'Source code and content released under the <a href="/license/">MIT license</a>.'

COMMENTS_ON_PAGES = True
USE_AUTHOR_CARD = True
AUTHOR_CARD_AVATAR = '/images/default_avatar.png'
AUTHOR_CARD_ON_PAGES = True
AUTHOR_CARD_DESCRIPTION = '''Anarchist. Humanist. Activist. Egalitarian. Feminist. Hacker. Debian developer. Tor advocate &amp; node operator. Hyperpolyglot. Musician. Ex pro gamer. Cunt.'''
