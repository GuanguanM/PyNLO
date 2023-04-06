# -*- coding: utf-8 -*-
"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

#--- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(1, os.path.abspath('..'))

#!!!: modified to use bysource ordering (__dict__ instead of dir, check git diff after updates)
import autosummary as new_autosummary
from sphinx.ext import autosummary
autosummary.__dict__.update(new_autosummary.__dict__)

#--- Project information -----------------------------------------------------

project = 'PyNLO'
copyright = '{:}, PyNLO authors'.format(datetime.date.today().year)
author = 'PyNLO authors'

# The full version, including alpha/beta/rc tags
release = 'dev'


#--- General configuration ---------------------------------------------------
html_show_sourcelink = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.viewcode",
    "nbsphinx",
]

autodoc_default_options = {
    'show-inheritance':True,
    "member-order": "bysource",
    }

autosummary_generate = True # Turn on sphinx.ext.autosummary
autosummary_ignore_module_all = False # Use __all__

numpydoc_show_class_members = False
numpydoc_show_inherited_class_members = False
# Report warnings for all validation checks
# numpydoc_validation_checks = {"all"}


nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
    ]

master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


#--- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_logo = "_static/pynlo.svg"
html_theme_options = {
    "show_toc_level": 2,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
