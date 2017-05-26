#!/bin/python3
# -*- coding: UTF-8 -*-

# 高斯完全主元素消元法矩阵的创建
import math
f = open(r"Gauss_data.txt")
s = f.readline().split()
s = list(map(int,s))
row = int(s[0])
row = row + 1
col = row
X = [0] * (col-1)
Matrix = []
for i in range(0,row-1):
	line = f.readline().split()
	line = list(map(float,line))
	Matrix.append(line)
f.close()
matrix = [0] * col
for i in range(0,col-1):
	matrix[i] = i + 1
Matrix.append(matrix)
# 消元
for k in range(0,col-2):
	ii,jj = k,k
	temp = Matrix[k][k]
	for i in range(k,row-1):
		for j in range(col-1):
			if math.fabs(temp) < math.fabs(Matrix[i][j]):
				temp = Matrix[i][j]
				ii,jj = i,j
	if ii!=k or jj!=k:
		Matrix[k],Matrix[ii] = Matrix[ii],Matrix[k]
		for q in range(0,row):
			Matrix[q][k],Matrix[q][jj] = Matrix[q][jj],Matrix[q][k]
	for r in range(k+1,row-1):
		L = Matrix[r][k] / Matrix[k][k]
		for c in range(k,col):
			Matrix[r][c] -= L * Matrix[k][c]
	for m in Matrix:
		for m1 in m:
			print("%.3f" % m1,end=' ')
		print('\n')
	print()
# 回代
X[col-2] = Matrix[row-2][col-1] / Matrix[row-2][col-2]
for k in range(col-3,-1,-1):
	a = 0
	for j in range(col-2,k,-1):
		a += Matrix[k][j] * X[j]
	X[k] = (Matrix[k][col-1]-a) / Matrix[k][k]

for j in range(0,col-1):
	i1 = int(Matrix[row-1][j])
	print(i1,"%.3f" % X[j])
