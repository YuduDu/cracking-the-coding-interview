#!/usr/bin/python
from LinkedList import LinkedList

def remove_duplicate(LList):
	this_node = LList.get_root()
	tmp = []
	while this_node:
		d = this_node.get_data()
		if d not in tmp:
			tmp.append(d)
		else:
			LList.remove(d)
		this_node = this_node.get_next()
	return LList
	

def remove_duplicate_follow_up(LList):
	this_node = LList.get_root()
	result = LinkedList()
	while this_node:
		d = this_node.get_data()
		if not result.find(d):
			result.add_tail(d)
		this_node = this_node.get_next()

	return result
	
	
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
list = remove_duplicate_follow_up(list)
list.printList()