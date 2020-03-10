import unittest
from prosecode.chunk import keyvalue

class TestKeyValueExtraction(unittest.TestCase):
    def testkv(self):
        s  = '{ hide cmd=true what=something output=html}'
        self.assertEqual(keyvalue(s, 'cmd'), True)
        self.assertEqual(keyvalue(s, 'hide'), True)
        self.assertEqual(keyvalue(s, 'hid'), False)
        self.assertEqual(keyvalue(s, 'hider'), False)
        self.assertEqual(keyvalue(s, 'what'), 'something')
        self.assertEqual(keyvalue(s, 'output'), 'html')

    def testquotedkeys(self):
        s  = '{id="quoted"}'
        self.assertEqual(keyvalue(s, 'id'), 'quoted')

    def testsymbols_in_ids(self):
        s  = '{ hide cmd=true id=_graph.graph output=html}'
        self.assertEqual(keyvalue(s, 'cmd'), True)
        self.assertEqual(keyvalue(s, 'id'), '_graph.graph')

    def testspaces(self):
        s = '{ id="_graph.graph_01" continue  = "_graph.graph_00" cmd}'
        self.assertEqual(keyvalue(s, 'id'), '_graph.graph_01')
        self.assertEqual(keyvalue(s, 'continue'), '_graph.graph_00')

if __name__ == '__main__':
    unittest.main()
