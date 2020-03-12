import unittest
from prosecode.weave import latexweave, htmlweave


class TestWeave(unittest.TestCase):
    def testweave(self):
        latex = latexweave(MD1, False)
        self.assertEqual(latex, EXPECTED_LATEX_MD1)
        latex = latexweave(MD1)
        self.assertEqual(latex, EXPECTED_LATEX_MD1)


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


if __name__ == '__main__':
    unittest.main()
