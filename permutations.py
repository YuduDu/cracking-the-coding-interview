
def permutations_add_one(source,c):
	result = []
	if source == []:
		result.append(c)
	else:
		for item in source:
			for i in range(0,len(item)+1):
				word = item[:i]+c+item[i:]
				result.append(word)
	return result
				


def permutations(s):
	result = []
	for c in s:
		result = permutations_add_one(result, c)
	return result

print permutations("abcde")