import unittest
from Node import *
from Btree import *

class MyTestCase(unittest.TestCase):

    def testsearch_in_node(self):
        print("#---------TEST search_in_node TEST---------#")
        print("#-------------------START------------------#")
        node = Node([],[],None,True)
        i = 0
        node.insert_value_in_node(20)
        node.insert_value_in_node(12)
        node.insert_value_in_node(13)
        node.insert_value_in_node(19)
        node.insert_value_in_node(32)
        self.assertFalse(node.search_in_node(18))
        self.assertTrue(node.search_in_node(20))
        self.assertTrue(node.search_in_node(12))
        self.assertTrue(node.search_in_node(13))
        self.assertTrue(node.search_in_node(19))
        self.assertTrue(node.search_in_node(32))
        print("#------------------FINISH------------------#")
        print()

    def testinsert_value_in_node(self):
        print("#---------TEST insert_value_in_node TEST---------#")
        print("#----------------------START---------------------#")
        node = Node([],[],None,True)
        node.insert_value_in_node(20)
        node.insert_value_in_node(12)
        node.insert_value_in_node(13)
        node.insert_value_in_node(19)
        node.insert_value_in_node(32)
        self.assertEqual(len(node.keys), 5)
        self.assertEqual(node.keys, [12, 13, 19, 20, 32])
        print("#---------------------FINISH---------------------#")
        print()

    def test_hauteur(self):
        print("#-------------TEST hauteur TEST------------#")
        print("#-------------------START------------------#")
        node = Node([],[],None,False)
        fils_gauche = Node([],[],None,False)
        fils_droit = Node([],[],None,False)
        petit_fils_gauche_g = Node([],[],None,True)
        petit_fils_gauche_d = Node([],[],None,True)
        petit_fils_droit_g = Node([],[],None,True)
        petit_fils_droit_d = Node([],[],None,True)
        node.sons.append(fils_gauche)
        node.sons.append(fils_droit)
        fils_gauche.sons.append(petit_fils_gauche_g)
        fils_gauche.sons.append(petit_fils_gauche_d)
        fils_droit.sons.append(petit_fils_droit_g)
        fils_droit.sons.append(petit_fils_droit_d)
        petit_fils_gauche_d.set_leaf()
        petit_fils_gauche_g.set_leaf()
        petit_fils_droit_d.set_leaf()
        petit_fils_droit_g.set_leaf()
        self.assertEqual(node.hauteur(), 2)
        print("#------------------FINISH------------------#")
        print()


if __name__ == '__main__':
    unittest.main()
