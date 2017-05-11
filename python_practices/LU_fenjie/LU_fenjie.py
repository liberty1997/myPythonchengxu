#!/bin/python3
# -*- coding: UTF-8 -*-

f = open(r"LU_data.txt")
r = f.readline().split()
row = int(r[0])
X = [0] * row
Y = [0] * row
Matrix = []
for i in range(0,row):
	line = f.readline().split()
	line = list(map(float,line))
	Matrix.append(line)
B = f.readline().split()
B = list(map(float,B))
f.close()

for i in range(1,row):
	Matrix[i][0] = Matrix[i][0] / Matrix[0][0]
for i in range(1,row):
	for j in range(i,row):
		t = 0
		for t1 in range(0,i):
			t += (Matrix[i][t1] * Matrix[t1][j])
		Matrix[i][j] -= t
	for k in range(i+1,row):
		l = 0
		for t2 in range(0,i):
			l += (Matrix[k][t2] * Matrix[t2][k-1])
		Matrix[k][i] = (Matrix[k][i] - l) / Matrix[i][i]

for m in Matrix:
	for m1 in m:
		print(m1,end=' ')
	print()
print()

Y[0] = B[0]
for i in range(1,row):
	t = 0
	for j in range(0,i):
		t += (Y[j] * Matrix[i][j])
	Y[i] = B[i] - t

for k in range(row-1,-1,-1):
	a = 0
	for j in range(row-1,k,-1):
		a += Matrix[k][j] * X[j]
	X[k] = (Y[k] - a) / Matrix[k][k]

for i,x in enumerate(X):
	print(i+1,x)
