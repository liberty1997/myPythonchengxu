#!/bin/python3
# -*- coding: UTF-8 -*-
import math
f = open(r'LeastSquareFitting_data.txt')
lines = f.readlines()
X = []
Y = []
N = 0 # 拟合次数
for line in lines:
	line = line.split()
	if len(line) == 1:
		N = int(line[0])
		break
	X.append(float(line[0]))
	Y.append(float(line[1]))
f.close()

print('X: ',X)
print('Y: ',Y)
a = [0] * (N+1)
Matrix = [[0 for c in range(N+2)] for r in range(N+1)]
# 因为此处的Matrix为对称矩阵,所以先求上三角
for r in range(N+1):
	t = r * 2
	for c in range(r,N+1):
		for i in range(len(X)):
			Matrix[r][c] += X[i]**(t)
		t += 1
# 然后填充下三角
for r in range(1,N+1):
	for c in range(r):
		Matrix[r][c] = Matrix[c][r]
# 求矩阵的最后一列
for r in range(N+1):
	for i in range(len(X)):
		Matrix[r][N+1] = Matrix[r][N+1] + Y[i] * X[i]**r
# 高斯完全主元素消元法
Matrix.append([i for i in range(N+2)])
for k in range(N):
	ii,jj = k,k
	t = Matrix[k][k]
	for i in range(k,N+1):
		for j in range(N+1):
			if math.fabs(t) < math.fabs(Matrix[i][j]):
				t = Matrix[i][j]
				ii,jj = i,j
	if ii!=k or jj!=k:
		Matrix[k],Matrix[ii] = Matrix[ii],Matrix[k]
		for q in range(N+2):
			Matrix[q][k],Matrix[q][jj] = Matrix[q][jj],Matrix[q][k]
	for r in range(k+1,N+1):
		L = Matrix[r][k] / Matrix[k][k]
		for c in range(k,N+2):
			Matrix[r][c] -= L * Matrix[k][c]
# 回代
a[Matrix[N+1][N]] = Matrix[N][N+1] / Matrix[N][N]
for k in range(N-1,-1,-1):
	t = 0
	for j in range(N,k,-1):
		t += Matrix[k][j] * a[Matrix[N+1][j]]
	a[Matrix[N+1][k]] = (Matrix[k][N+1]-t) / Matrix[k][k]
# 拟合方程
print('拟合方程:\ny=%.5f' % a[0],end='')
for i in range(1,len(a)):
	print('{:+.5f}x^{}'.format(a[i],i),end='')
# 误差平方和
I = 0
for i in range(len(X)):
	y = 0
	for j in range(len(a)):
		y += a[j] * X[i]**j
	I += (y-Y[i])**2
print('\n误差平方和: {}'.format(I))
