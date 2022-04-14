#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Richard Styron'
SITENAME = 'Rocks and Water'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Archives', 'archives.html'),
#         )

# Social widget
SOCIAL = None
#GITHUB_USERNAME = 'cossatot'
#TWITTER_USERNAME = 'earthanalysis'

#DISQUS_SITENAME = 'rocksandwater'
#DISQUS_SHORTNAME = 'rocksandwater'
#GOOGLE_ANALYTICS = 'UA-46638714-1'


MENUITEMS = [('About', '/about/'),
             ('Bio', '/bio/'),
             ('Research', '/research/'),
             ('Publications', '/publications/'),
             ('Global Block Model', '/global-block-model/'),
             ('Archives', '/archives.html'),
             ]

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

SHOW_ARCHIVES = True
ARCHIVES_SAVE_AS = "archives.html"


DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs', 'uploads', 'js']
NOTEBOOK_DIR = 'content/notebooks'

MARKUP = ('md', 'ipynb')

#plugins
PLUGIN_PATHS= ["../pelican-plugins/", "plugins"]
PLUGINS = ['ipynb.liquid', 
           'render_math',
           'liquid_tags.video',
           #'pelican_javascript',
           #'pelican-dynamic',
           'summary']#, 'liquid_tags.notebook']

THEME = 'themes/new'
#THEME = '../themes/pelican-octopress-theme'
