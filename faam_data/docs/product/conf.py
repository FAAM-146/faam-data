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
import os
import json


def setup(app):
    app.add_css_file('faam.css')


def get_product_name():
    with open(os.environ['FAAM_PRODUCT'], 'r') as f:
        data = json.load(f)
    return data['meta']['long_name']


def get_version():
    return os.environ['PRODUCT_VERSION']


# -- Project information -----------------------------------------------------
project = get_product_name()
copyright = f'{datetime.datetime.now().year}, FAAM'
author = 'FAAM'
release = get_version()
version = get_version()

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

napoleon_include_init_with_doc = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'base_rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_static_path = ['../static']
html_logo = '../static/faam-small.png'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
latex_elements = {
    'papersize': 'a4paper',
    'extraclassoptions': 'openany,oneside',
    'preamble': r'''
        \definecolor{FAAMDarkBlue}{HTML}{252243}
        \definecolor{FAAMLightBlue}{HTML}{0ABBEF}
        \usepackage{eso-pic}
        \usepackage{pict2e}
        \newcommand\BackgroundPic{
        \put(300,-260){
            \color{FAAMLightBlue}\circle*{900}
        }
        \put(300,-260){
            \color{FAAMDarkBlue}\circle*{760}
        }
    }''',
    # Pretty hacky this - escaping from the sphinx macros,
    # but it sorta kinda works well enough.
    'maketitle': '''
        \\AddToShipoutPicture*{{\\BackgroundPic}}
        \\begin{{titlepage}}
            \\color{{FAAMDarkBlue}}
            \\begin{{flushright}}
                \\sphinxlogo
                {{\\sffamily
                    {{\\Huge \\textbf{{ {project} }}}}
                    \\par\\vspace{{1cm}}
                    {{\\itshape\\LARGE\\textbf{{ Release {release} }}}}
                    \\par\\vspace{{3cm}}
                    {{\\LARGE \\textbf{{{author}}}}}
                    \\par\\vspace{{3cm}}
                    {{\\Large \\textbf{{{date}}}}}
                 }}
             \\end{{flushright}}
        \\end{{titlepage}}
        '''.format(
            project=project,
            release=release,
            author=author,
            date=datetime.date.today().strftime('%B %-d, %Y')
        )
}
latex_logo = '../static/faam.png'
