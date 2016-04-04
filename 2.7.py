#!/usr/bin/python

from LinkedList import LinkedList
	
def palindrome(l):
	if l.get_size()<=1:
		return True
	s = []
	slow = fast = l.get_root()
	s.append(slow.get_data())
	while (slow and fast and fast.get_next()):
		slow = slow.get_next()
		s.append(slow.get_data())
		fast = fast.get_next().get_next()
	
	if fast:
		s.pop()
		
	slow = slow.get_next()
	while slow:

		t = s.pop()

		if (slow.get_data() != t):
			return False
		slow = slow.get_next()
	return True
	
list = LinkedList()					
list.add_tail('A')
list.add_tail('B')
list.add_tail('C')
list.add_tail('D')
list.add_tail('E')
list.add_tail('D')
list.add_tail('C')
list.add_tail('B')
list.add_tail('A')
print palindrome(list)