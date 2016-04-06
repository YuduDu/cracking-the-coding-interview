#!/usr/bin/python

def quickSort(list):
	if(len(list)<=1):
		return list
	pivot = list[0]
	less = []
	greater = []
	for i in list[1:]:
		if i<=pivot:
			less.append(i)
		else:
			greater.append(i)
			
	less = quickSort(less)
	greater = quickSort(greater)
	
	return less+[pivot]+greater
		
alist = [54,26,93,17,77,31,44,55,20]
print quickSort(alist)