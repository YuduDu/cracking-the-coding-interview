#!/usr/bin/python

from LinkedList import LinkedList

def detectLoop(l):
	if l.get_size()<=0:
		return False
	
	slow = fast = l.get_root()
	while (slow and fast and fast.get_next()):
		slow = slow.get_next()
		fast = fast.get_next().get_next()
		
		if slow == fast:
			fast = l.get_root()
			while (slow and fast):
				slow = slow.get_next()
				fast = fast.get_next()
				if slow == fast:
					return slow
list = LinkedList()					
list.add_tail('A')
list.add_tail('B')
list.add_tail('C')
list.add_tail('D')
list.add_tail('E')
list.get_root().get_next().get_next().get_next().get_next().set_next(list.get_root().get_next().get_next())


point = detectLoop(list)
print point.get_data()