# -*- coding: utf-8 -*-
#
# libLAS documentation build configuration file, created by
# sphinx-quickstart on Mon Mar 30 11:04:44 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('../python'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [  'sphinx.ext.autodoc',
                'sphinx.ext.doctest',
                'sphinx.ext.intersphinx',
                'sphinx.ext.todo',
                'sphinx.ext.ifconfig',
                'rst2pdf.pdfbuilder',
                ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'docs'

# General information about the project.
project = u'libLAS'
copyright = u'2016, Howard Butler, Mateusz Loskot and others'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

def read_version(filename):
    # oh yes, this is brittle
    data = open(filename).readlines()
    major = 'LIBLAS_VERSION_MAJOR'
    minor = 'LIBLAS_VERSION_MINOR'
    patch = 'LIBLAS_VERSION_PATCH'

    for line in data:
        if str(major) in line:
            line = line.replace('SET('+major+' ', '')
            line = line.replace(')','')
            line = line.replace('"','')
            maj = line.strip()
        if str(minor) in line:
            line = line.replace('SET('+minor+' ', '')
            line = line.replace(')','')
            line = line.replace('"','')
            min = line.strip()
        if str(patch) in line:
            line = line.replace('SET('+patch+' ', '')
            line = line.replace(')','')
            line = line.replace('"','')
            pat = line.strip()
    return '%s.%s.%s'%(maj, min, pat)

version = read_version('../CMakeLists.txt')

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

html_style = 'sphinx.css'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {'rightsidebar':True}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'liblas.org'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Documentation'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
"index":["indexsidebar.html",'searchbox.html'],
"docs":['globaltoc.html',"indexsidebar.html",'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'libLASdoc'


breathe_projects = {
    "liblas":"/Users/hobu/hg/liblas-cmake/doc/api/xml"
    }

breathe_default_project = "liblas"


pdf_documents = [
    ('docs', u'libLAS', u'libLAS Documentation', u'The libLAS Team'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['liblas']
pdf_language = "en_US"
pdf_fit_mode = "overflow"
pdf_use_toc = True
pdf_splittables = True
pdf_appendices = []
pdf_baseurl = 'http://liblas.org'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
