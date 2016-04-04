#!/usr/bin/python

#!/usr/bin/python

from LinkedList import Node

class Queue(object):

	def __init__(self):
		self.head = None
		
	def push(self,data):
		new_node = Node(data)
		this_node = self.head
		if not this_node:
			self.head = new_node
			
		else:
			while this_node.get_next() != None:
				this_node = this_node.get_next()
				
			this_node.set_next(new_node)
		
	def pop(self):
		data = self.head.get_data()
		self.head = self.head.get_next()
		return data
	
	def peek(self):
		return self.head.get_data()
		
		

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print queue.pop()
print queue.pop()