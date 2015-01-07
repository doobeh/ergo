#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anthony Plunkett'
SITENAME = u'ergo.io'
SITEURL = 'http://ergo.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'
PLUGIN_PATHS = ['plugins']
DEFAULT_LANG = u'en'
THEME = r'theme'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
BOOTSTRAP_THEME = 'stanley'
SOCIAL = False
HIDE_SIDEBAR = True
PYGMENTS_STYLE = 'pastie'
USE_PAGER = True
RESPONSIVE_IMAGES = True

STATIC_PATHS = ["images", ]

PLUGINS = [
    'pelican_gist',
    'pelican_youtube',
    'pelican_vimeo',
    'series',
    'sitemap',
    # 'better_figures_and_images',
]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
