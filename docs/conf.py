# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
import sys

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

numfig = True
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

from django.conf import settings
from django.utils import timezone

import django
django.setup()


sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'djangodocs',
    'doc_extensions',
    'sphinx_tabs.tabs',
#    'sphinxcontrib.googleanalytics',
]
templates_path = ['_templates']

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'index'
project = u'BTK2.0'
copyright = '2015-{}, Kenichi Kumatani, Rita Singh, Bhiksha Raj'.format(
    timezone.now().year
)
version = '2.7'
release = version
exclude_patterns = ['_build']
default_role = 'obj'
intersphinx_mapping = {
    'python': ('http://python.readthedocs.io/en/latest/', None),
    'django': ('http://django.readthedocs.io/en/1.9.x/', None),
    'sphinx': ('http://sphinx.readthedocs.io/en/latest/', None),
}
htmlhelp_basename = 'btk_two_point_o'
latex_documents = [
    ('index', 'btk_two_point_o.tex', u'BTK2.0',
     u'Kenichi Kumatani, Rita Singh, Bhiksha Raj', 'manual'),
]
man_pages = [
    ('index', 'btk_two_point_o_docs', u'BTK2.0',
     [u'Kenichi Kumatani, Rita Singh, Bhiksha Raj'], 1)
]

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = 'img/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# Activate autosectionlabel plugin
autosectionlabel_prefix_document = True
