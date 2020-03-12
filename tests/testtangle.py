import unittest
import os
from pyfakefs.fake_filesystem_unittest import TestCase
from prosecode.tangle import tangle, cleanup

class TestTangle(TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        self.file_path = '/prose/example.md'
        self.srcdir = '/src/'
        self.keepit = self.srcdir + 'keepit.py'
        self.twoparts = self.srcdir + 'twoparts.py'
        self.dontkeepit = self.srcdir + 'dontkeepit.py'
        self.fs.create_dir(self.srcdir)
        self.fs.create_file(self.file_path, contents = EXAMPLE_MD)

    def testtangle(self):
        tangle(self.file_path, self.srcdir)
        self.assertTrue(os.path.exists(self.keepit))
        self.assertTrue(os.path.exists(self.twoparts))
        self.assertFalse(os.path.exists(self.dontkeepit))
        with open(self.keepit) as f:
            self.assertEqual('Good\n', f.read())
        with open(self.twoparts) as f:
            self.assertEqual('Part 1\n\nPart 2\n', f.read())

    def testcleanup(self):
        tangle(self.file_path, self.srcdir)
        self.assertTrue(os.path.exists(self.keepit))
        self.assertTrue(os.path.exists(self.twoparts))
        cleanup(self.file_path, self.srcdir)
        self.assertFalse(os.path.exists(self.keepit))
        self.assertFalse(os.path.exists(self.twoparts))

EXAMPLE_MD = """
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

if __name__ == '__main__':
    unittest.main()
