#!/usr/bin/python

# find minimum element of a rotated (sorted array)

def binary_search(list,h,t):
	if h > t:
		return False
	elif h ==t:
		return list[h]
	else:
		m = (h+t)/2
		if list[m]>=list[t]:
			result = binary_search(list,m+1,t)
		else:
			result = binary_search(list,h,m)
		return result

def find_min(list):
	#check input format
	if len(list) == 0:
		return None
	elif len(list) ==1:
		return list[0]
	
	# init
	h = 0
	t = len(list)-1
	return binary_search(list,h,t)

print find_min([3,4,5,6,7,1,2])