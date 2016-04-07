#!/usr/bin/python

#BST:
	# 1. insert data
	# 2. find data
	# 3. preorder()
	# 4. inorder()
	# 5. postorder()



class Node(object):
		
	def __init__(self,data):
		self.value = data
		self.left = None
		self.right = None
		
	def insert(self,data):
		if self.value == data:
			return False
		elif self.value < data:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True
		else:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
	
	def find(self,data):
		if self.value == data:
			return True
		elif self.value > data:
			return self.left.find(data)
		else:
			return self.right.find(data)
			
	def preorder(self):
		print self.value
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()
			
	def inorder(self):
		if self.left:
			self.left.inorder()
		print self.value
		if self.right:
			self.right.inorder()

	def postorder(self):
		if self.left:
			self.left.postorder()
		if self.right:
			self.right.postorder()
		print self.value
	
	def get_h(self):
		if self.left:
			left = self.left.get_h()
		else:
			left = 0
		if self.right:
			right = self.right.get_h()
		else:
			right = 0
			
		return max(left,right)+1

class BST(object):
		
	def __init__(self):
		self.root = None
		
	def insert(self,data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True
		
	def find(self,data):
		if self.root:
			return self.root.find(data)
		else:
			return False
		
	def preorder(self):
		if self.root:
			self.root.preorder()
			
	def inorder(self):
		if self.root:
			self.root.inorder()
	
	def postorder(self):
		if self.root:
			self.root.postorder()
			
	def get_root(self):
		return self.root
	
	def get_height(self):
		if self.root == None:
			return 0
		else:
			return self.root.get_h()
			

		
#btree = BST()
#btree.insert(8)
#btree.insert(4)
#btree.insert(3)
#btree.insert(10)
#btree.insert(9)
#btree.insert(13)
#btree.insert(11)
#btree.insert(15)
#btree.insert(16)

#btree.postorder()

