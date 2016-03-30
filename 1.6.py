def rotate(M,n):
	Result = [[0 for i in range(n)] for i in range(n)]
	for j in range(n):
		for i in range(n):
			Result[i][n-1-j]=M[j][i] 
	return Result

s = raw_input('input your matrix, space between elements in row, ; between rows')
m = s.split(';')
for i in range(len(m)):
	m[i]= m[i].split()
	if len(m[i]) != len(m):
		print False
		quit()
print m

print rotate(m,len(m))