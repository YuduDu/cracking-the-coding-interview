#!/usr/bin/python

from LinkedList import LinkedList

def sum(L1, L2):
	node1 = L1.get_root()
	node2 = L2.get_root()
	result = LinkedList()
	i = 0
	
	while node1 and node2:
		n1 = node1.get_data()
		n2 = node2.get_data()

		r = (n1+n2+i)%10
		i = (n1+n2+i)/10
		
		result.add_tail(r)
		node1 = node1.get_next()
		node2 = node2.get_next()
	
	while node1:
		result.add_tail(node1.get_data())
		node1 = node1.get_next()

	while node2:
		result.add_tail(node2.get_data())
		node2 = node2.get_next()
	
	return result

L1 = LinkedList()
L1.add_tail(7)
L1.add_tail(1)
L1.add_tail(6)
L2 = LinkedList()
L2.add_tail(5)
L2.add_tail(9)
L2.add_tail(2)
L = sum(L1,L2)
L.printList()
