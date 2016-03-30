#!/usr/bin/python

import random

def sort(list):
	if len(list)<=1:
		return list
	tmp = [0]*131
	result = []
	for item in list:
		tmp[item]+=1
		
	for i in range(130,0,-1):
		while tmp[i]>0:
			result.append(i)
			tmp[i]-=1
	return result
	
#list  = [random.randint(0,130) for r in range(0,1000)]
#print list
print sort([3,23])