#!/usr/bin/python

def compress(s):
	if (len(s) <= 2):
		return s
	else:
		tmp = s[0]
		count = 1
		result = ""
		for c in s[1:]:
			if c == tmp:
				count+=1
			else:
				result = result+tmp+str(count)
				tmp=c
				count =1
		result = result+tmp+str(count)
		if len(result)>=len(s):
			return s
		else:
			return result


s = raw_input("input your string: ")
print compress(s)