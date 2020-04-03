import markdown
from prosecode.tangle import tangle
from prosecode.htmltolatexparser import HTMLtoLaTeX
from prosecode.chunk_extension import CodeChunkExtension
from prosecode.displaymath_extension import DisplayMathExtension
import os.path

def htmlweave(md, execute = False, executepath = os.path.curdir):
    """
    Produce HTML (as a string) from a string containing markdown.

    If `executed` is set to True, then all code chunks in the file will be
    executed.

    By default the code will not be executed.
    """
    displaymath = DisplayMathExtension()
    codechunks = CodeChunkExtension(execute = execute,
                                    executepath = executepath)

    html = markdown.markdown(md, extensions=[codechunks,
                                             displaymath,
                                             'tables',
                                             ])

    return html

def latexweave(md, execute = False, executepath = os.path.curdir):
    """
    Produce LaTeX (as a string) from a string containing markdown.

    If `executed` is set to True, then all code chunks in the file will be
    executed.

    By default the code will not be executed.
    """
    parser = HTMLtoLaTeX()
    html = htmlweave(md, execute, executepath)
    parser.feed(html)
    return ''.join(parser.latex)
