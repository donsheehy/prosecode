========
Examples
========

Consider the following simple markdown file, `sample.md`.

.. code-block:: md

  # Sample Markdown

  ## Get excited!

  ```python {cmd id="_itscode"}
  x = 2
  print(x +3)
  ```

We can tangle out the code with the following command.

.. code-block::

  prosecode tangle sample.md


This will produce a file called `itscode.py` that looks as follows.

.. code-block:: python

  x = 2
  print(x +3)

Then, we can weave the code into proper LaTeX as follows.

.. code-block::

  prosecode weave sample.md

This produces the file `sample.tex`.

.. code-block:: latex

  \chapter{Sample Markdown}

  \section{Get excited!}

  \begin{Verbatim}[commandchars=\\\{\}]
  \PY{n}{x} \PY{o}{=} \PY{l+m+mi}{2}
  \PY{n+nb}{print}\PY{p}{(}\PY{n}{x} \PY{o}{+}\PY{l+m+mi}{3}\PY{p}{)}
  \end{Verbatim}
