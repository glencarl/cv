# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cv'
copyright = '2025, Glen CARL'
author = 'Glen CARL'
version = '0.1.0'
release = '0.1.0'

language = 'en'
pygments_style = 'sphinx'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'classic'
html_theme = 'pydata_sphinx_theme'
# requires pip install pydata-sphinx-theme

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

primary_color = '#162956'
sec_blue_color = '#2E5590'
sec_light_blue_color = '#6DA9CF'
sec_gray_color = '#4C4F59'
sec_yellow_color = '#FAB208'
sec_code_color = '#E7E7E7'

# for classic
# html_theme_options = {
#                      'rightsidebar': True,
#                      'stickysidebar': True,
#                      'collapsiblesidebar': False,
#                      'externalrefs': True,
#                      'footerbgcolor': sec_gray_color,
#                      'sidebarbgcolor': primary_color,
#                      'relbarbgcolor': sec_blue_color,
#                      'codebgcolor': sec_code_color,
#                     }

# for pydata_sphinx_theme
html_theme_options = {
                      'navbar_end': ['theme-switcher', 'navbar-icon-links'],
                     }

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/GlenCarlsm.jpg"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/0cogFav.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
