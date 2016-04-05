#!/usr/bin/python

class SetOfStacks(object):
	
	def __init__(self,data = None):
		self.top = 5
		stack = [data]
		self.size = 1
		self.sets = [stack]
	
	def push(self, data):
		
		if self.size <self.top:
			self.sets[-1].append(data)
			self.size += 1
		else:
			stack = [data]
			self.size = 1
			self.sets.append(stack)
	
	def pop(self):
		if self.size == 1:
			data = self.sets[-1].pop()
			self.sets.pop()
			self.size = self.top
		else :
			data = self.sets[-1].pop()
			self.size-=1
		return data
	
	def peek(self):
		return self.sets[-1][-1]
	def getsets(self):
		return self.sets


stacks = SetOfStacks()

for i in range(10):
	stacks.push(i)

for i in range(5):
	print stacks.pop()
print stacks.getsets()

