#!/usr/bin/python

from BinarySearchTree import BST,Node

btree = BST()
btree.insert(8)
btree.insert(4)
btree.insert(3)
btree.insert(10)
btree.insert(9)
btree.insert(13)
btree.insert(11)
btree.insert(15)
btree.insert(16)

class solution(object):
	last_value = None
	
	def check(self,node):
		if node == None:
			return True
		else:
			if not self.check(node.left):
				return False
			
			if (self.last_value >= node.value ):
				return False
			else:
				self.last_value = node.value
			
			if not self.check(node.right):
				return False
			
			return True
			
		
	def checkBinaryTree(self,tree):
		return self.check(tree.root)

s = solution()

print s.checkBinaryTree(btree)

