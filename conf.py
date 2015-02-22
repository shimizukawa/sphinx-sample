# -*- coding: utf-8 -*-

master_doc = 'index'

project = u'sphinx-sample'
copyright = u'2013, sphinx-sample'
version = '1.0'
release = '1.0'
language = 'ja'
exclude_patterns = ['_build', '_build_sample']
html_theme = 'default'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'sphinx-sample.tex', u'sphinx-sample Documentation',
   u'sphinx-sample', 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'sphinx-sample', u'sphinx-sample Documentation',
     [u'sphinx-sample'], 1)
]

