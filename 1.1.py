#!/usr/bin/python

def unique(s):
	if (type(s)is not str) or (s==""):
		return False
	tmp=""
	for c in s:
		if c in tmp:
			return False
		else:
			tmp+=c
	return True

print unique("thise")