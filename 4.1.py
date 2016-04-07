#!/usr/bin/python
from BinarySearchTree import BST,Node

def checkBalance(root):
	if root:
	   return balanceH(root)>=0

def balanceH(node):
	if node == None:
		return 0
	else:
		left = balanceH(node.left)
		right = balanceH(node.right)
		if left<0 or right<0 or abs(left-right)>1:
			return -1
		
		return max(left,right)+1
		
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
btree.postorder()
root = btree.get_root()
print checkBalance(root)