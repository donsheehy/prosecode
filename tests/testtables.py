import unittest
from prosecode.weave import latexweave

class TestTable(unittest.TestCase):
    def testtable3col(self):
        print(latexweave(MD))


MD = """\

| h1          | h2      | h3 |
|-----|-----------|:------:|
| 1,1 | 1,2 | 1,3 |
| 2,1 | 2,2 | 2,3 |

"""

EXPECTED_LATEX = """\
\\begin{tabular}{c c c}
\\hline

\\hline
1,1 & 1,2 & 1,3 \\\\
2,1 & 2,2 & 2,3 \\\\
\\end{tabular}
"""


if __name__ == '__main__':
    unittest.main()
