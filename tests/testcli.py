import unittest
import os
from click.testing import CliRunner
from  prosecode.cli import tangle, weave, cleanup, styledefs


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.md1 = 'md1.md'
        self.md2 = 'md2.md'
        self.md3 = 'md3.md'
        self.md3_tex = 'md3.tex'
        self.srcdir = 'src/'
        self.itscode = self.srcdir + 'itscode.py'
        self.keepit = self.srcdir + 'keepit.py'
        self.twoparts = self.srcdir + 'twoparts.py'
        self.dontkeepit = self.srcdir + 'dontkeepit.py'

    def _create_file(self, filename, contents):
        with open(filename, 'w') as f:
            f.write(contents)

    def testtangle_MD1(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            self._create_file(self.md1, MD1)
            os.mkdir(self.srcdir)
            runner.invoke(tangle, [self.md1, '--srcdir', self.srcdir])
            self.assertTrue(os.path.exists(self.itscode))
            with open(self.itscode) as f:
                self.assertEqual('x = 2\nprint(x +3)\n', f.read())

    def testtangle_MD2(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            self._create_file(self.md2, MD2)
            os.mkdir(self.srcdir)
            result = runner.invoke(tangle, [self.md2, '--srcdir', self.srcdir])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.exists(self.keepit))
            self.assertTrue(os.path.exists(self.twoparts))
            self.assertFalse(os.path.exists(self.dontkeepit))
            with open(self.keepit) as f:
                self.assertEqual('Good\n', f.read())
            with open(self.twoparts) as f:
                self.assertEqual('Part 1\n\nPart 2\n', f.read())

    def testcleanup(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            self._create_file(self.md2, MD2)
            os.mkdir(self.srcdir)
            runner.invoke(tangle, [self.md2, '--srcdir', self.srcdir])
            self.assertTrue(os.path.exists(self.keepit))
            self.assertTrue(os.path.exists(self.twoparts))
            result = runner.invoke(cleanup, [self.md2, '--srcdir', self.srcdir])
            print(result.exception)
            self.assertEqual(result.exit_code, 0)
            self.assertFalse(os.path.exists(self.keepit))
            self.assertFalse(os.path.exists(self.twoparts))

    def testweave(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            self._create_file(self.md3, MD3)

            self.assertTrue(os.path.exists(self.md3))
            result = runner.invoke(weave, [self.md3])
            self.assertTrue(os.path.exists(self.md3))
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.exists(self.md3_tex))
            with open (self.md3_tex) as f:
                self.assertEqual(EXPECTED_LATEX_MD3, f.read())

MD1 = """
# Sample Markdown

## Get excited!

```python {cmd id="_itscode"}
x = 2
print(x +3)
```
"""

MD2 = """
## Header

```python {cmd id="_keepit"}
Good
```

```python {cmd id="_twoparts_01"}
Part 1
```

```python {cmd id="dontkeepit"}
bad
```

```python {cmd id="_twoparts_02" continue="_twoparts_01"}
Part 2
```
"""

MD3 = """
# H1

## H2

\\[
    x = 1
\\]
"""

EXPECTED_LATEX_MD3 = """\
\chapter{H1}

\section{H2}


\\[
    x = 1
\\]
"""



if __name__ == '__main__':
    unittest.main()
