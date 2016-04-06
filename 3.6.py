#!/usr/bin/python

class stack(object):
	def __init__ (self):
		self.list = []

	def push(self,data):
		self.list.append(data)

	def pop(self):
		return self.list.pop()

	def peek(self):
		return self.list[-1]

	def isEmpty(self):
		if len(self.list) == 0:
			return True
		else: return False

	def get_stack(self):
		return self.list

def insert(s, data):
	if s.isEmpty():
		s.push(data)
	else:
		top = s.peek()
		if data >= top:
			s.push(data)
		else:
			tmp = s.pop()
			s = insert(s,data)
			s.push(tmp)
	return s

def sort(s):
	if not s.isEmpty():
		tmp = s.pop()
		s = sort(s)
		s = insert(s,tmp)
	return s

# set a stack
s = stack()
s.push(2)
s.push(3)
s.push(79)
s.push(45)
s.push(23)
s.push(11)
s.push(78)

print s.get_stack()

s = sort(s)

print s.get_stack()


