# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Standard library imports
import datetime
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
# Reader imports
from src import dsc

# -- Project information -----------------------------------------------------

project = "Data Science Common"
author = "Ryan Kelley, Randall Kelley"
version = dsc.__version__
release = dsc.__version__
this_year = datetime.date.today().year
copyright = "%s, %s" % (this_year, author)

# The full version, including alpha/beta/rc tags
releases_release_uri = (
    f"https://github.com/LiveRamp/lr-research-core/releases/tag/{version}"
)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["../../dsc/util/test_*"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
