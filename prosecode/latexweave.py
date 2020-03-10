from html.parser import HTMLParser
from prosecode.tangle import tangle

h_to_l = {
    'h1': '\\chapter{',
    'h2': '\\section{',
    'h3': '\\subsection{',
    'h4': '\\subsubsection{',
    'h5': '\\paragraph{',
    'pre': '\\begin{verbatim}',
    'code': '',
    'p': '\n\n',
}

close_h_to_l = {
    'h1': '}\n\n',
    'h2': '}\n\n',
    'h3': '}\n\n',
    'h4': '}\n\n',
    'h5': '}\n\n',
    'pre': '\\end{verbatim}\n\n',
    'code': '',
    'p': '\n',
}

class HTMLtoLaTeX(HTMLParser):
    def __init__(self, latex):
        super().__init__()
        self.latex = latex

    def handle_starttag(self, tag, attrs):
        self.latex.append(h_to_l[tag])

    def handle_endtag(self, tag):
        self.latex.append(close_h_to_l[tag])

    def handle_data(self, data):
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
