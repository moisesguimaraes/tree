#!/usr/bin/python
'''
Created on 06/09/2013

@author: moisesguimaraes
'''
import unittest, random
from tree import Node, Tree


class NodeTestCase(unittest.TestCase):
    
    def test001(self):
        node = Node(42)
        
        self.assertIsNotNone(node)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        

class TreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()

    def test001(self):
        # creation
        self.assertIsNotNone(self.tree)
        self.assertIsNone(self.tree.root)

    def test002(self):
        # insert
        self.tree.insert(42)
        self.assertEqual(self.tree.root.data, 42)
        
        self.tree.insert(25)
        self.assertEqual(self.tree.root.left.data, 25)
        
        self.tree.insert(777)
        self.assertEqual(self.tree.root.right.data, 777)
        
    def test003(self):
        # length
        for i in range(1, 10):
            self.tree.insert(i)
            self.assertEqual(i, len(self.tree))
        
    def test004(self):
        # iterators
        self.tree.insert([4, 2, 1, 3, 6, 5, 8, 7, 9])
            
        self.assertEqual([4, 2, 1, 3, 6, 5, 8, 7, 9], [n.data for n in self.tree.preorder()])    
        self.assertEqual([1, 3, 2, 5, 7, 9, 8, 6, 4], [n.data for n in self.tree.posorder()])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], [n.data for n in self.tree.inorder()])
            
    def test005(self):
        # simple remove
        self.tree.insert([42, 25, 777])
        
        self.tree.remove(0)
        self.assertEqual(len(self.tree), 3)
        
        self.tree.remove(777)
        self.assertEqual(len(self.tree), 2)
        
        self.assertEqual([42, 25], [n.data for n in self.tree.preorder()])
            
        self.tree.insert(12)
        self.assertEqual(len(self.tree), 3)

        self.tree.remove(25)
        self.assertEqual(len(self.tree), 2)
        
        self.assertEqual([42, 12], [n.data for n in self.tree.preorder()])
        
    def test006(self):
        # complex remove
        self.tree.insert([42, 25, 777, 12, 36, 555, 999, 600])
            
        self.tree.remove(42)
        self.assertEqual(self.tree.root.data, 555)
        
        self.tree.remove(555)
        self.assertEqual(self.tree.root.data, 600)
            
    def test007(self):
        # stress
        data = range(10, 100)
        random.shuffle(data)
        
        tree = Tree(data)
        self.assertEqual(len(tree), len(data))
        
        random.shuffle(data)
        
        for d in data:
            tree.remove(d)
            
        self.assertEqual(len(tree), 0)
        
if __name__ == '__main__':
    unittest.main()