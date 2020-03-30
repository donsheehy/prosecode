from html.parser import HTMLParser
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter


h_to_l = {
    'h1': '\\chapter{',
    'h2': '\\section{',
    'h3': '\\subsection{',
    'h4': '\\subsubsection{',
    'h5': '\\paragraph{',
    'code.lang-verbatim': '\\begin{Verbatim}\n',
    'code.lang-python': '',
    'code': '\\texttt{',
    'pre': '',
    'pre.prettyprint': '',
    'p': '\n',
    'strong': '\\textbf{',
    'em': '\\emph{',
    'u': '\\underline{',
    'br': '\\\\',
    'ol': '\\begin{enumerate}\n',
    'ul': '\\begin{itemize}\n',
    'li': '\\item ',
    'blockquote': '\\begin{quote}',
    'img': '\\includegraphics[width=\\textwidth]{./',
    'table': '\\begin{tabular}{c c c c}\n',
    'thead': '\\hline\n',
    'th': '',
    'tr': '',
    'td': '',
    'tbody': '',
}

close_h_to_l = {
    'h1': '}\n',
    'h2': '}\n',
    'h3': '}\n',
    'h4': '}\n',
    'h5': '}\n',
    'code.lang-verbatim': '\n\\end{Verbatim}',
    'code.lang-python': '',
    'code': '}',
    'pre': '',
    'pre.prettyprint': '',
    'p': '\n',
    'strong': '}',
    'em': '}',
    'u': '}',
    'br': '',
    'img': '',
    'ol': '\\end{enumerate}',
    'ul': '\\end{itemize}',
    'li': '\n',
    'blockquote': '\\end{quote}',
    'table': '\\end{tabular}',
    'thead': '\\hline\n',
    'th': ' & ',
    'tr': '\\\\',
    'td': ' &' ,
    'tbody': '\\hline',
}

class HTMLtoLaTeX(HTMLParser):
    def __init__(self):
        super().__init__()
        self.latex = []
        self.mystack = []

    def handle_starttag(self, tag, attrs):
        attrs = {k : v for (k, v) in attrs}
        if 'class' in attrs:
            tag = tag + '.' + attrs['class']
        self.latex.append(h_to_l[tag])
        if tag == 'img':
            # print("image:", tag, attrs)
            filename = attrs['src'].replace('.svg', '.pdf')
            self.latex.append(filename)
            self.latex.append('}')
        self.mystack.append(tag)

    def handle_endtag(self, tag):
        if self.mystack[-1] in ['code.lang-verbatim', 'code.lang-python']:
            tag = self.mystack[-1]
        self.latex.append(close_h_to_l[tag])
        self.mystack.pop()

    def handle_data(self, data):
        if self.mystack:
            tag = self.mystack[-1]
            if tag == 'code.lang-python':
                data = (_codecomment(data) +
                        highlight(data, PythonLexer(), LatexFormatter()))
            elif tag == 'code':
                data = _latexescape(data)
            elif tag == 'code.lang-verbatim':
                data = _unescape(data)

        self.latex.append(data)

def _latexescape(txt):
    txt = txt.replace('_', '\\_')
    txt = txt.replace('&', '\&')
    txt = txt.replace('^', '\\ensuremath{\\wedge}')
    return txt

def _codecomment(txt):
    output = []
    for line in txt.split('\n'):
        output.extend(['% ', line, '\n'])
    return "".join(output)

def _unescape(txt):
    txt = txt.replace('&amp;', '&')
    txt = txt.replace('&lt;', '<')
    txt = txt.replace('&gt;', '>')
    txt = txt.replace('&quot;', '"')
    return txt
