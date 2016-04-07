#!/usr/bin/python
def radixSort(list):
	if len(list)<=1:
		return list

	radix = 10
	replacement = 1

	max_size = False

	while not max_size:
		max_size = True

		bucket = [[] for i in range(radix)]
		for i in list:
			tmp = i/replacement
			l = tmp%radix
			#print i
			#print l
			bucket[l].append(i)
			if max_size and (tmp>0):
				max_size = False

		n = 0
		#print bucket
		for m in bucket:
			while len(m)>0:
				list[n]=m.pop(0)
				n+=1
		#print list
		replacement *=radix
		
	return list
	
list = [1,323,23,555,4444444,134123,1325,567,679,780,8,8,756,45,345,333334,64565,123]
print radixSort(list)