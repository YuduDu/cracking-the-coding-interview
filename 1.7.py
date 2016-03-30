#!/usr/bin/python

def set_zero(M,i,j,r,c):
	M[i]=[0]*c
	for m in range(r):
		M[m][j]=0
	return M

def find_zero(M,r,c):
	R = [i for i in range(r)]
	
	for j in range(c):
		print "j"+str(j)
		for i in R:
			if M[i][j] == 0:
				M = set_zero(M,i,j,r,c)
				#print "j"+str(j)+"i"+str(i)
				R.remove(i)
				break
	return M

M = [[0,2,3],[4,5,6],[7,0,9],[10,11,12]]
r = 4
c =3
print find_zero(M, r, c)