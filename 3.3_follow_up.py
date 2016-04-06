#!/usr/bin/python

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
	def popAt(self,i):
		try:
			self.sets[i]
		except:
			return "index not exist"
	
		if (len(self.sets[i])==0):
			return False
		elif i == len(self.sets)-1:
			self.pop()
		else:
			if len(self.sets[i]) ==1:
				data = self.sets[i].pop()
				self.sets.pop(i)
			else:
				data = self.sets[i].pop()
				
			return data
			


stacks = SetOfStacks()

for i in range(30):
	stacks.push(i)
	
print stacks.getsets()


for i in range(3):
	print stacks.popAt(i)
	print stacks.popAt(5)
print stacks.popAt(5)
print stacks.popAt(5)
print stacks.getsets()

