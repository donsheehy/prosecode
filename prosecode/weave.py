import markdown
from prosecode.tangle import tangle
from prosecode.htmltolatexparser import HTMLtoLaTeX
from prosecode.chunk_extension import CodeChunkExtension
from prosecode.displaymath_extension import DisplayMathExtension

def htmlweave(mdfile, execute = True):
    md = open(mdfile, 'r').read()
    displaymath = DisplayMathExtension()
    codechunks = CodeChunkExtension(execute = execute)
    html = markdown.markdown(md, extensions=[codechunks,
                                             displaymath,
                                             'tables',
                                             ])
    return html

def latexweave(mdfile, execute = True, outfilename = None):
    """
    Produce a LaTeX file from a markdown file.

    All code chunks in the file will be executed.
    """
    if outfilename is None:
        outfilename = mdfile.replace('.md', '.tex')

    html = htmlweave(mdfile, execute)
    latex = []
    parser = HTMLtoLaTeX(latex)
    parser.feed(html)
    with open(outfilename, 'w') as outfile:
        for line in latex:
            outfile.write(line)
