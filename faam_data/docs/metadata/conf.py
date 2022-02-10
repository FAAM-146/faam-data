# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import os
#import sys
#sys.path.insert(0, os.path.abspath('../../..'))
import sphinx_rtd_theme # type: ignore
import datetime

#print(sys.path[0])
#from faam_data import __version__
__version__ = 0.1

def setup(app):
    app.add_css_file('mods.css')

# -- Project information -----------------------------------------------------

project = 'FAAM Data: Attribute Conventions'
copyright = f'{datetime.datetime.now().year}, FAAM'
author = 'FAAM'
release = f'{__version__}'
version = f'{__version__}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon'
]

napoleon_include_init_with_doc = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'base_rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../static']
#latex_toplevel_sectioning = 'section'
latex_elements = {
    'papersize': 'a4paper',
    'extraclassoptions': 'openany,oneside',
}
latex_logo = '../static/faam.png'
