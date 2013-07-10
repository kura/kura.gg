#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kura'
SITENAME = u'kura.io'
SITEURL = 'http://kura.io/new'

THEME = 'kura.io'
TIMEZONE = 'Europe/Paris'

GITHUB_URL = 'https://github.com/kura'
TWITTER_URL = 'https://twitter.com/kuramanga'
DISQUS_SITENAME = "syslogtv"

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = "feeds/atom.xml"
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_RSS = "feeds/rss.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
CATEGORY_FEED_RSS = "feeds/%s.rss.xml"
TAG_FEED_ATOM = "feeds/%s.atom.xml"
TAG_FEED_RSS = "feeds/%s.rss.xml"

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

STATIC_PATHS = ['images', 'files', 'slides']

PDF_GENERATOR = True
PDF_STYLE = "twelvepoint"
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
EXTRA_PATH_METADATA = {
    'files': {'path': 'files'},
}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATH = "plugins/"
PLUGINS = [
    # ...
    'pelican_gist',
    'archive_unique_dates',
    'sitemap',
    'gzip_cache',
    # ...
]

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
    }
}
