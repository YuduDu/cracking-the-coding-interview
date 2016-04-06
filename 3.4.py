#!/usr/bin/python
class tower(object):
	def __init__(self):
		self.stack = []

	def push(self, data):
		if len(self.stack)==0:
			self.stack.append(data)
		elif data < self.peek():
			self.stack.append(data)
			return True
		else:
			return False

	def peek(self):
		return self.stack[-1]

	def pop(self):
		return self.stack.pop()
		
	def get_tower(self):
		return self.stack
		
	def get_size(self):
		return len(self.stack)

class towersOfHanol(object):
	def __init__(self,N):
		tower1 = tower()
		tower2 = tower()
		tower3 = tower()
		for i in range(N,0,-1):
			tower1.push(i)
		self.Hanol = [tower1,tower2,tower3]

	def move(self,source,target):
		if (source not in range(3)) or (target not in range(3)):
			return False
		
		elif self.Hanol[source].get_size() == 0:
			return False

		else:
			data = self.Hanol[source].pop()
			if self.Hanol[target].push(data):
				return True
			else:
				return False
				
	def getHanol(self):
		for i in self.Hanol:
			print i.get_tower()


def moveHanol(hanol,N,source,target,buffer):
	if N == 1:
		hanol.move(source,target)
	else:
		moveHanol(hanol,N-1,source,buffer,target)
		hanol.move(source,target)
		moveHanol(hanol,N-1,buffer,target,source)


hanol = towersOfHanol(20)
hanol.getHanol()
moveHanol(hanol,20,0,2,1)
print "result:"
hanol.getHanol()
