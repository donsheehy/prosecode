import unittest
import os
from pyfakefs.fake_filesystem_unittest import TestCase
from prosecode.tangle import tangle

class TestTangle(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def testtangle(self):
        file_path = '/prose/example.md'
        srcdir = '/src/'
        self.fs.create_dir(srcdir)
        self.fs.create_file(file_path, contents = EXAMPLE_MD)
        tangle(file_path, srcdir)
        self.assertTrue(os.path.exists(srcdir + 'keepit.py'))
        self.assertFalse(os.path.exists(srcdir + 'dontkeepit.py'))

    def testcleanup(self):
        pass

EXAMPLE_MD = """
## Header

```python {cmd id="_keepit"}
Good
```

```python {cmd id="dontkeepit"}
bad
```
"""

if __name__ == '__main__':
    unittest.main()
