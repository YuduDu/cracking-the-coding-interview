#!/usr/bin/python
from BinarySearchTree import BST,Node

def generateBST(list,tree = None):
	if tree == None:
		tree = BST()
	if len(list) == 0:
		return tree
	else:
		mid = len(list)/2
		mNum = list[mid]
		tree.insert(mNum)
		tree = generateBST(list[:mid],tree)
		tree = generateBST(list[mid+1:],tree)
		return tree
		
list=[1,2,3,4,5,6,7,8]
tree = generateBST(list)
print tree.get_height()