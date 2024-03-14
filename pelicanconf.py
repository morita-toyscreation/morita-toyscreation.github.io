#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ToysCreation.Inc'
SITEURL = 'https://www.toyscreation.jp'
RELATIVE_URLS = True
SITENAME = 'ToysCreation'
SITETITLE = SITENAME
SITESUBTITLE = 'トイズクリエイション'
SITEDESCRIPTION = '%s\'s トイズクリエイションはWEBサイト、スマートフォン、ソーシャルゲームの受託開発・自社製品開発を行うクリエイティブ・プロダクションです。' % AUTHOR
SITELOGO = '/images/toyscreation.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = "../pelican-themes/Flex"
STATIC_PATHS = ['images', 'static']
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'

# Translate to Japan.
DEFAULT_LANG = 'ja'
OG_LOCALE = 'ja_JP'
LOCALE = 'ja_JP'

DATE_FORMATS = {
    'ja': '%Y年%-m月%-d日',
}

# Default theme language.
I18N_TEMPLATES_LANG = 'ja'

# CC_LICENSE = {
#     'name': 'Creative Commons Attribution-ShareAlike',
#     'version': '4.0',
#     'slug': 'by-sa'
# }

COPYRIGHT_YEAR = "2014-2024"

DEFAULT_PAGINATION = 10

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
HOME_HIDE_TAGS = True

# LINKS = (('Portfolio', '#'),)

# SOCIAL = (('linkedin', '#'),
#           ('github', '#'),
#           ('google', '#'),
#           ('twitter', 'gakushi0130'),
#           ('rss', '#'))

SOCIAL = (('twitter', 'https://twitter.com/ToysCreation'),
          ('rss', 'https://qiita.com/morita-toyscreation'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# DISQUS_SITENAME = ''
ADD_THIS_ID = 'ra-5aae0f0fc99eb630'
GOOGLE_ANALYTICS = 'UA-55971269-1'
# GOOGLE_TAG_MANAGER = ''
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'design': 6, 'rumid': 1234 }

# Enable i18n plugin.
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
