#!/bin/python3
# -*- coding: UTF-8 -*-

f = open(r"Gauss_data.txt")
s = f.readline().split()
s = list(map(int,s))
row,col = s[0],s[1]
X = [0] * (col-1)
Matrix = []
for i in range(0,row):
	line = f.readline().split()
	line = list(map(float,line))
	Matrix.append(line)
f.close()

for k in range(0,col-2):
	for r in range(k+1,row):
		L = Matrix[r][k] / Matrix[k][k]
		for c in range(k,col):
			Matrix[r][c] -= L * Matrix[k][c]
	for m in Matrix:
		for m1 in m:
			print(m1,end=' ')
		print('\n')
	print()

X[col-2] = Matrix[row-1][col-1] / Matrix[row-1][col-2]
for k in range(col-3,-1,-1):
	a = 0
	for j in range(col-2,k,-1):
		a += Matrix[k][j] * X[j]
	X[k] = (Matrix[k][col-1]-a) / Matrix[k][k]

for i,x in enumerate(X):
	print(i+1,x)
