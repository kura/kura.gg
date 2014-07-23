#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kura'
SITENAME = 'kura.io'
SITEURL = 'https://kura.io'

THEME = 'ghastly'
# THEME = 'kura.io'

TIMEZONE = 'Europe/London'

GITHUB_URL = 'https://github.com/kura'
TWITTER_URL = 'https://twitter.com/kuramanga'
DISQUS_SITENAME = "syslogtv"

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%d %b %Y'

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT
}

MENUITEMS = ()

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CATEGORY_URL = 'c/{slug}'
CATEGORY_SAVE_AS = 'c/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 't/{slug}'
TAG_SAVE_AS = 't/{slug}/index.html'

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

SUMMARY_MAX_LENGTH = 75

STATIC_PATHS = ['images', 'files', 'slides', 'extra/robots.txt',
                'extra/favicon.ico', ]

EXTRA_PATH_METADATA = {
    'files': {'path': 'files'},
    'images': {'path': 'images'},
    'slides': {'path': 'slides'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

DIRECT_TEMPLATES = (('index', 'archives', '404'))

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins/", ]
PLUGINS = [
    'assets',
    'extract_toc',
    'pelican_fontawesome',
    'pelican_gist',
    'pelican_vimeo',
    'pelican_youtube',
]
