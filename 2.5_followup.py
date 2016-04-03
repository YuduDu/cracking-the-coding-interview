#!/usr/bin/python

from LinkedList import LinkedList

def toint(l):
	this = l.get_root()
	n = l.get_size()
	N = 0
	while this:
		n-=1
		N += this.get_data()*(10**n)
		this = this.get_next()
	return N

def toList(n):
	result = LinkedList()
	t = n/10
	while t>0:
		result.add_head(n%10)
		n = t
		t = n/10
	result.add_head(n%10)
	return result


def sum(L1, L2):
	n1 = toint(L1)
	n2 = toint(L2)
	n = n1+n2
	return toList(n)

L1 = LinkedList()
L1.add_head(7)
L1.add_head(1)
L1.add_head(6)

L2 = LinkedList()
L2.add_head(5)
L2.add_head(9)
L2.add_head(2)
L = sum(L1,L2)
L.printList()