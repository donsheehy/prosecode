=========================
Using prosecode with make
=========================

For a large project with multiple files, it is recommended that you use make to manage the build.
Here is an example `Makefile`.

This assumes the markdown files are in a folder called `prose/`.
The .tex files will be placed in a folder called `tex/`.
The code will be placed in a folder called `package/`.

.. code-block:: basemake

  SRCDIR = mypackage/
  MD:= $(wildcard prose/*.md)
  TEX:= $(MD:prose/%.md=tex/%.tex)

  .PHONY: help Makefile pdf clean weave

  tex/pygments_macros.tex :
  	prosecode styledefs --outfile tex/pygments_macros.tex

  tex/%.tex: prose/%.md
  	prosecode tangle $< --srcdir $(SRCDIR)
  	prosecode weave $< --outfile $@ --execute True

  clean:
    $(foreach mdfile, $(MD), prosecode cleanup $(mdfile) --srcdir $(SRCDIR);)

  weave: $(TEX)

  pdf: $(TEX) tex/main.tex tex/pygments_macros.tex
  	cd tex; pdflatex main.tex
