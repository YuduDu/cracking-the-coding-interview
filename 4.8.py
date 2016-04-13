#!/usr/bin/python



def findSub(tree1, tree2):
	if tree2 == None:
		return True
	return subTree(tree1, tree2)

def subTree(tree1,tree2):
	if tree1 == None:
		return False
	
	if tree1.value == tree2.value:
		if matchTree(tree1, tree2):
			return True

	return (subTree(tree1.left, tree2) or subtree(tree1.right, tree2));

def matchTree(tree1, tree2):
	if (tree1 ==None) and (tree2==None):
		return True
	
	if (tree1 == None) or (tree2 == None):
		return False

	if tree1.value != tree2.value:
		return False
	
	return (matchTree(tree1.right, tree2.right) and matchTree(tree1.left, tree2.left))
