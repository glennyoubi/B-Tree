import unittest
from Node import *
from Btree import *




class Btree_test(unittest.TestCase):


    def testsearch_test_empty_tree(self):
        root = Node([],[],None,False)
        arbre = Btree(2,3,root)
        self.assertFalse(arbre.btree_search(2))
        self.assertFalse(arbre.btree_search(3))
        self.assertFalse(arbre.btree_search(1))
    
    def testsearch_test_empty_tree_value_in_tree(self):
        root = Node([],[],None,False)
        arbre = Btree(2,3,root)
        l = [i for i in range(1,11)]
        for v in l:
            arbre.insert(v)
        self.assertTrue(arbre.btree_search(2))
        self.assertTrue(arbre.btree_search(3))
        self.assertTrue(arbre.btree_search(1))
    
    def testsearch_test_empty_tree_value_not_in_tree(self):
        root = Node([],[],None,False)
        arbre = Btree(2,3,root)
        l = [i for i in range(1,11)]
        for v in l:
            arbre.insert(v)
        self.assertFalse(arbre.btree_search(13))
        self.assertFalse(arbre.btree_search(12))
        self.assertFalse(arbre.btree_search(11))
    
if __name__ == '__main__':
    unittest.main()
