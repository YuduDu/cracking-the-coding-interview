#!/usr/bin/python

class Node(object):
		
		def __init__(self, d, n =None):
			self.data =d
			self.next_node = n

		def get_next(self):
			return self.next_node
		
		def set_next(self,n):
			self.next_node = n

		def get_data(self):
			return self.data

		def set_data(self, d):
			self.data = d

class LinkedList(object):

		def __init__(self, r = None):
			self.root = r
			if r == None:
				self.size = 0
			else:
				self.size =1

		def get_size(self):
			return self.size
		
		def add_node(self,node):
			if self.root !=None:
				s = self.root
				while s.get_next() != None:
					s=s.get_next() 
				s.set_next(node)
			else:
				self.root = node
			
			self.size = self._size()
			
		def _size(self):
			this_node = self.root
			size = 0
			while this_node:
				size +=1
				this_node = this_node.get_next()
			return size
			
		def add_head(self, d):
			new_node = Node(d,self.root)
			self.root = new_node
			self.size+=1

		def add_tail(self, d):
			new_node = Node(d)
			if self.root !=None:
				s = self.root
				while s.get_next() != None:
					s=s.get_next() 
				s.set_next(new_node)
			else:
				self.root = new_node
			self.size+=1

		def remove (self, d):
			this_node = self.root
			prev_node = None
			
			while this_node:
				if this_node.get_data() == d:
					if prev_node:
						prev_node.set_next(this_node.get_next())
					else:
						self.root = this_node.get_next()
					self.size -=1
					return True
				else:
					prev_node = this_node
					this_node = this_node.get_next()
			return False

		def find (self,d):
			this_node = self.root
			while this_node:
				if this_node.get_data() == d:
					return d
				else:
					this_node = this_node.get_next()
			return None

		def printList(self):
			this_node = self.root
			while this_node:
				print this_node.get_data()
				this_node = this_node.get_next()
				
		def get_root(self):
			return self.root


#
#mylist = LinkedList()
##mylist.add_head(1)
#mylist.add_head(2)
#mylist.add_head(3)
#mylist.add_tail(4)
#mylist.printList()