#!/usr/bin/python
'''
Created on 06/09/2013

@author: moisesguimaraes
'''
import sys

class Node(object):

    def __init__(self, data):
        self.data   = data
        self.left   = None
        self.right  = None

    def __str__(self):
        return str(self.data)

class Tree:
    
    def __init__(self, data = None):
        self.root = None
        
        if data:
            self.insert(data)
        
        
    def _insert(self, node, data):
        if not node:
            return Node(data)
            
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
            
        return node


    def insert(self, data):
        if type(data) == type([]):
            for d in data:
                self.insert(d)
        else:
            self.root = self._insert(self.root, data)
        
        
    def _remove(self, node, data):
        if node:
            if data == node.data:
                if not node.left or not node.right:
                    node = node.left or node.right
                else:
                    next = node.right
                    
                    while next.left:
                        next = next.left
                        
                    node.data = next.data
                    node.right = self._remove(node.right, next.data) 
                    
            elif data < node.data:
                node.left = self._remove(node.left, data)
            else:
                node.right = self._remove(node.right, data)
            
        return node

                
    def remove(self, data):
        if type(data) == type([]):
            for d in data:
                self.remove(d)
        else:
            self.root = self._remove(self.root, data)
        
            
    def _preorder(self, root):
        if root:
            yield root
            for l in self._preorder(root.left):  yield l
            for r in self._preorder(root.right): yield r

        
    def preorder(self):
        return self._preorder(self.root)
        
        
    def _posorder(self, root):
        if root:
            for l in self._posorder(root.left):  yield l
            for r in self._posorder(root.right): yield r
            yield root


    def posorder(self):
        return self._posorder(self.root)
        
        
    def _inorder(self, root):
        if root:
            for l in self._inorder(root.left):  yield l
            yield root
            for r in self._inorder(root.right): yield r


    def inorder(self):
        return self._inorder(self.root)
        

    def __len__(self):
        return sum(1 for _ in self.preorder())
        
        
    def __str__(self):
        def add_prefix(prefix, node):
            return add_prefix(prefix + 2, node.right) \
                 + '\n' + '   ' * prefix + str(node)  \
                 + add_prefix(prefix + 2, node.left)  if node else ''
                 
        return add_prefix(0, self.root)
        

def main():
    tree = Tree()
    
    for arg in sys.argv[1:]:
        try:
            n = int(arg)
            
            if n > 0:
                tree.insert(n)
            else:
                tree.remove(-n)
        
        except:
            arg = arg.upper()
            
            if arg == 'PRE':
                print ', '.join([str(node.data) for node in tree.preorder()])
                
            elif arg == 'POS':
                print ', '.join([str(node.data) for node in tree.posorder()])
                
            elif arg == 'IN':
                print ', '.join([str(node.data) for node in tree.inorder()])
                
            elif arg == 'GRA':
                print '\n', '-' * 70,
                print tree


if __name__ == '__main__':
    main()
