#!/usr/bin/python

from BinarySearchTree import BST,Node
from LinkedList import LinkedList,Node

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

#btree.postorder()


class solution():
	list = []
	def traverse(self,tree):
		if tree.root:
			self.findnodes(tree.root, 0)
			return self.list
		else:
			return None

	def findnodes(self,node,level):
		if len(self.list) < level+1:
			ll = LinkedList()
			self.list.append(ll)
		
		self.list[level].add_head(node.value)
		if node.left:
			self.findnodes(node.left,level+1)
		if node.right:
			self.findnodes(node.right,level+1)

s = solution()
result = s.traverse(btree)

for i in result:
	i.printList()
	