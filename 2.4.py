#!/usr/bin/python

from LinkedList import LinkedList
def partition (LList, x):
	this_node = LList.get_root()
	smaller = LinkedList()
	larger = LinkedList()
	while this_node:
		if this_node.get_data() < x:
			smaller.add_tail(this_node.get_data())
		else:
			larger.add_tail(this_node.get_data())
		this_node = this_node.get_next()
	smaller.add_node(larger.get_root())
	return smaller

list = LinkedList()
list.add_tail(1)
list.add_tail(2)
list.add_tail(3)
list.add_tail(4)
list.add_tail(3)
list.add_tail(5)
list.add_tail(2)
list.printList()
print "partition"
list = partition(list, 4)
list.printList()