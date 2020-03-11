==================
Building the LaTeX
==================

Prosecode attempts to build relatively minimal LaTeX.
If you want to then build the produced LaTeX into a pdf, you would `\input` the generated file into some other LaTeX source.
For example, the following wraps `file1` and `file2` as chapters in a book.

.. code-block:: latex

  \documentclass{book}
  \usepackage{amsmath,amsthm,amssymb}
  \usepackage{fancyvrb}
  \usepackage{color}
  \usepackage{graphicx}
  \usepackage{etoolbox} % Only used for block quotes.

  \input{pygments_macros}

  \begin{document}
    \input{titlepage}
    \tableofcontents
    \input{file1}
    \input{file2}
  \end{document}
