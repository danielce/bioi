#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Admin'
SITENAME = 'bio-industrie-op-school.nl'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'pl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = [
    'extended_sitemap',
    'neighbors',
]

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/home/daniel/projects/pelican/themes/clean-blog"
BIO = "Fanatyk mody"
PROFILE_IMAGE = "avatar.jpg"
SITESUBTITLE = "Strona domowa"
HEADER_IMAGE = "images/lego_background.jpg"
PLUGIN_PATHS = ['../pelican-plugins/', ]
