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

DISPLAY_PAGES_ON_MENU = False

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = (('blackhole.io', 'http://blackhole.io'),
             ('pypipins', 'https://pypip.in'),
             ('apt-security', ''),
             ('rabbitmq-nagios', ''),
             ('PyBozo', ''),
             ('Am I Secure?', 'http://kura.io/pages/amisecure.html'))

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
