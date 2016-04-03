#!/usr/bin/python

def isSubstring(s1,s2):
	if len(s1)!=len(s2):
		return False
	s = s1*2
	if s2 in s:
		return True
	else:
		return False

print isSubstring("erbottlewat","waterbottle")