import unittest
from prosecode.tangle import tangle

class TestTangle(unittest.TestCase):
    def testtangle(self):
        tangled = tangle(EXAMPLE_MD)
        self.assertTrue('keepit' in tangled)
        self.assertTrue('twoparts' in tangled)
        self.assertTrue('dontkeepit' not in tangled)
        self.assertEqual('Good\n', tangled['keepit'].fullstr())
        print(str(tangled['twoparts']))
        self.assertEqual('Part 1\n\nPart 2\n', tangled['twoparts'].fullstr())

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
