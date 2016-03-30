#!/usr/bin/python


def dictionary(s):
	dict={}
	for c in s:
		if c in dict.keys():
			dict[c]+=1
		else:
			dict[c] = 1
	return dict

def permutation(s1,s2):
	if (type(s1) is not str) or (type(s2) is not str) or (s1 == "") or (len(s1)!=len(s2)):
		return False
	dict1 = dictionary(s1)
	dict2 = dictionary(s2)

	for key,value in dict1.items():
		try:
			if (key not in dict2.keys()) or (value != dict2[key]):
				return False
		except:
			return False
	
	return True
			
	
print permutation("abcdefg", "efgagbdc")