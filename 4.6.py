#!/usr/bin/python

def leftmost(node):
	if node:
		if node.left:
			leftmost(node.left)
		else:
			return node
	
def inorderSucc(node):
	if node == None:
		return None
		
	if node.right:
		return leftmost(node.right)
		
	else:
		n = node
		p = node.parent
		while p and (p.left is not n):
			n = p
			p = p.parent
		return n
			