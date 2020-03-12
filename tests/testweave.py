import unittest
from prosecode.weave import latexweave, htmlweave


class TestWeave(unittest.TestCase):
    def testlatexweave(self):
        latex = latexweave(MD1, False)
        self.assertEqual(latex, EXPECTED_LATEX_MD1)
        latex = latexweave(MD1)
        self.assertEqual(latex, EXPECTED_LATEX_MD1)

    def testhtmlweave(self):
        html = htmlweave(MD1, False)
        self.assertEqual(html, EXPECTED_HTML_MD1)
        latex = htmlweave(MD1)
        self.assertEqual(html, EXPECTED_HTML_MD1)

    def testlatexweave_withcode(self):
        latex = latexweave(MD2, False)
        self.assertEqual(latex, EXPECTED_TEX_MD2)
        latex = latexweave(MD2, True)
        self.assertEqual(latex, EXPECTED_TEX_MD2_EXECUTED)


    def testhtmlweave_withcode(self):
        html = htmlweave(MD2, False)
        self.assertEqual(html, EXPECTED_HTML_MD2)
        html = htmlweave(MD2, True)
        # print(html)
        self.assertEqual(html, EXPECTED_HTML_MD2_EXECUTED)

MD1 = """\
# H1

## H2

\\[
    x = 1
\\]
"""

EXPECTED_LATEX_MD1 = """\
\chapter{H1}

\section{H2}


\\[
    x = 1
\\]
"""

EXPECTED_HTML_MD1 = """\
<h1>H1</h1>
<h2>H2</h2>
<p>\\[
    x = 1
\\]</p>\
"""

MD2 = """\
```python {cmd}
print('Hello, World!')
```
"""

EXPECTED_HTML_MD2 = """\
<pre class="prettyprint"><code class="lang-python">print('Hello, World!')
</code></pre>\
"""

EXPECTED_HTML_MD2_EXECUTED = """\
<p><pre class="prettyprint"><code class="lang-python">print('Hello, World!')
</code></pre>
<pre class="prettyprint"><code class="lang-verbatim">Hello, World!
</code></pre></p>\
"""

EXPECTED_TEX_MD2 = """\
% print('Hello, World!')
% \n\\begin{Verbatim}[commandchars=\\\\\\{\\}]
\\PY{n+nb}{print}\\PY{p}{(}\\PY{l+s+s1}{\\PYZsq{}}\\PY{l+s+s1}{Hello, World!}\\PY{l+s+s1}{\\PYZsq{}}\\PY{p}{)}
\\end{Verbatim}
"""
EXPECTED_TEX_MD2_EXECUTED = """
% print('Hello, World!')
% \n\\begin{Verbatim}[commandchars=\\\\\\{\\}]
\\PY{n+nb}{print}\\PY{p}{(}\\PY{l+s+s1}{\\PYZsq{}}\\PY{l+s+s1}{Hello, World!}\\PY{l+s+s1}{\\PYZsq{}}\\PY{p}{)}
\\end{Verbatim}

\\begin{Verbatim}
Hello, World!

\\end{Verbatim}
"""


if __name__ == '__main__':
    unittest.main()
