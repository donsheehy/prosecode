# Prose Code

### Literate programming in Python from markdown to LaTeX

The `prosecode` library is being developed as a way to generate really neat LaTeX from markdown files.
It will support both tangling and weaving code.
That is, it can run the code from the markdown files and it can also extract the code into separate `.py` files.

It is assumed that the markdown file uses github style fenced code blocks with extra data as is used in the Markdown-Preview-Enhanced plugin for Atom and VSCode.

## Installation (coming soon)

```
pip install prosecode
```

## Tangling

The following will extract the python code from `myfile.md` and store it in files.

```
$ prosecode tangle myfile.md
```

There is an optional `--srcdir` parameter that tells where to put the tangled source code.

```
$ prosecode tangle myfile.md --srcdir src/
```

## Weaving

The following will execute the code in `myfile.md`, place the output inline, and then convert it to LaTeX.

```
$ prosecode weave mdfile.md --execute=True --outfile someotherfile.tex
```

The `--outfile` parameter is optional.  If omitted, it will simply replace `.md` with `.tex`.

There is also an optional parameter `--execute` that tells whether or not to execute the code chunks.
The default value is false.
