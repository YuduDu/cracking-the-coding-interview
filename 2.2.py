#!/usr/bin/python

from LinkedList import LinkedList

def sublist(LList, k):
	if (k == 0) or (LList.get_size()<k) :
		return False
	this_node = LList.get_root()
	i = 1
	while this_node:
		if i == k:
			return this_node
		else:
			this_node = this_node.get_next()
			i+=1
	return False
		

list = LinkedList()
list.add_tail(1)
list.add_tail(2)
list.add_tail(3)
list.add_tail(4)
list.add_tail(3)
list.add_tail(5)
list.add_tail(2)
list.printList()
print " remove: "
node = sublist(list,10)
while node:
	print node.get_data()
	node =node.get_next()
