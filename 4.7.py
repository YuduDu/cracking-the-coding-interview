#!/usr/bin/python

from BinarySearchTree import BST,Node

def cover(root,node):
	if root == None:
		return False
	if root is node:
		return True
	return (cover(root.left,node) or cover(root.right,node))

def findAncestor(root,p,q):
	if root == None:
		return None
	if (root is p ) or (root is q):
		return root

	is_p_on_left = cover(root.left,p)
	is_q_on_left = cover(root.left,q)
	
	if not (is_p_on_left == is_q_on_left):
		return root
	else:
		if is_p_on_left:
			return findAncestor(root.left,p,q)
		else:
			return findAncestor(root.right,p,q)

def CommonAncestor(root, p, q):
	if cover(root,p) and cover(root,q):
		return findAncestor(root,p,q)
	else:
		return None



			
	
		
		