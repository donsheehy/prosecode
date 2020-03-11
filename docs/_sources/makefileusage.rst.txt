=========================
Using prosecode with make
=========================

For a large project with multiple files, it is recommended that you use make to manage the build.
Here is an example `Makefile`.

This assumes the markdown files are in a folder called `prose/`.

.. code-block:: basemake

  MD:= $(wildcard prose/*.md)
  TEX:= $(MD:prose/%.md=prose/tex/%.tex)

  .PHONY: help Makefile pdf

  prose/tex/%.tex: prose/%.md
  	prosecode tangle $< --srcdir src/
  	prosecode weave $< --outfile $@

  clean:
  	rm prose/tex/fullbook.*

  pdf: $(TEX) prose/tex/main.tex
  	cd prose/tex; pdflatex -jobname=fullbook main.tex
