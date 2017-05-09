#!/bin/python3
# -*- coding: UTF-8 -*-

row,col = map(int,input("请输入行数和列数:(i.e. 3 4) ").split())

print("请输入线性方程组的增广矩阵:")
print("Example:")
Example = [[2,8,2,14],[1,6,-1,13],[2,-1,2,5]]
for r in Example:
	for r1 in r:
		print(r1,end=' ')
	print('\n')

Matrix = []
X = [0] * (col-1)
for r in range(0,row):
	temp = []
	for c in range(0,col):
		temp.append(float(input()))
	Matrix.append(temp)

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
