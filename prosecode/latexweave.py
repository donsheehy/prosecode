from html.parser import HTMLParser
from prosecode.tangle import tangle
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter

h_to_l = {
    'h1': '\\chapter{',
    'h2': '\\section{',
    'h3': '\\subsection{',
    'h4': '\\subsubsection{',
    'h5': '\\paragraph{',
    'pre': '',
    'code': '',
    'p': '\n',
}

close_h_to_l = {
    'h1': '}\n',
    'h2': '}\n',
    'h3': '}\n',
    'h4': '}\n',
    'h5': '}\n',
    'pre': '',
    'code': '',
    'p': '\n',
}

class HTMLtoLaTeX(HTMLParser):
    def __init__(self, latex):
        super().__init__()
        self.latex = latex
        self.mystack = []

    def handle_starttag(self, tag, attrs):
        self.latex.append(h_to_l[tag])
        self.mystack.append(tag)

    def handle_endtag(self, tag):
        self.latex.append(close_h_to_l[tag])
        self.mystack.pop()

    def handle_data(self, data):
        if self.mystack and self.mystack[-1] == 'code':
            data = highlight(data, PythonLexer(), LatexFormatter())
        self.latex.append(data)


def weave(srcdir, mdfilename, destdir = ''):
    html = tangle(srcdir, mdfilename)
    latex = []
    parser = HTMLtoLaTeX(latex)
    parser.feed(html)
    texfilename = mdfilename.replace('.md', '.tex')
    with open(texfilename, 'w') as outfile:
        for line in latex:
            outfile.write(line)

if __name__ == '__main__':
    SRC_DIR = './examples/src/'
    MD_FILE = './examples/tangle.md'
    weave(SRC_DIR, MD_FILE)
