#!/usr/bin/env python3
#
# Deker documentation build configuration file, created by
# sphinx-quickstart on Sun Dec 25 18:07:21 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.

import os
import sys


project = "Deker local adapters"
copyright = "2023, OpenWeather"
author = "OpenWeather"

# Add support for auto-doc

# Ensure that sanic is present in the path, to allow sphinx-apidoc to
# autogenerate documentation from docstrings
sys.path.insert(0, os.path.abspath(".."))


# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "m2r2",
    "enum_tools.autoenum",
]

templates_path = ["_templates"]

# Enable support for both Restructured Text and Markdown
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# web page tab logo
# html_logo = "./_static/sanic-framework-logo-white-400x97.png"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = os.getenv("GITHUB_REF_NAME") if os.getenv("GITHUB_REF_TYPE", "") == "tag" else "latest"
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
#
# modules.rst is generated by sphinx-apidoc but is unused. This suppresses
# a warning about it.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "modules.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "analytics_id": "G-XXXXXXXXXX",  #  Provided by Google in your dashboard
    "analytics_anonymize_ip": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 5,
    "includehidden": True,
    "titles_only": False,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_css_files = ["custom.css"]
# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Dekerdoc"

# -- Custom Settings -------------------------------------------------------

suppress_warnings = ["image.nonlocal_uri"]


autodoc_typehints = "description"
autodoc_default_options = {
    "member-order": "groupwise",
}

intersphinx_mapping = {
    "deker": ("http://de1.owm.io:10000", None),
}
