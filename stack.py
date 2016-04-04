#!/usr/bin/python

from LinkedList import Node

class Stack(object):
	
	def __init__(self):
		self.head = None
		self._min =[]
		
	def push(self,data):
		new_node = Node(data, self.head)
		self.head = new_node
		if self._min ==[]:
			self._min.append(data)
		elif data <= self._min[-1]:
			self._min.append(data)
		
	def pop(self):
		data = self.head.get_data()
		self.head = self.head.get_next()
		if data == self._min[-1]:
			self._min.pop()
		return data
	
	def peek(self):
		return self.head.get_data()
		
	def min(self):
		return self._min[-1]
		
		

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(3)
stack.push(3)
stack.push(2)

print stack.min()
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()
print stack.pop()
print stack.min()