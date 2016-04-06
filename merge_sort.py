def merge(left,right):
	i = 0
	j = 0
	ll = len(left)
	lr = len(right)
	list=[]
	while (i < ll) and (j < lr):
		if left[i]<=right[i]:
			list.append(left[i])
			list.append(right[j])
		else:
			list.append(right[j])
			list.append(left[i])

		i+=1
		j+=1
	
	while i<ll:
		list.append(left[i])
		i+=1
	while j<lr:
		list.append(right[j])
		j+=1
	
	return list
	
def mergeSort(list):
	if len(list)<=1:
		return list
	else:
		m = len(list)/2
		left = list[:m]
		right = list[m:]

		left = mergeSort(left)
		right = mergeSort(right)
		list = merge(left,right)
		return list
		
		
alist = [54,26,93,17,77,31,44,55,20]
list =  mergeSort(alist)
print list