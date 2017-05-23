#!/bin/python3
# -*- coding: UTF-8 -*-
f = open(r'Lagrange_data.txt')
lines = f.readlines()
X = []
Y = []
for line in lines:
	line = line.split()
	line = list(map(float,line))
	X.append(line[0])
	Y.append(line[1])
f.close()

def func(x):
	L = []
	# 求L
	for i in range(len(X)):
		Fenzi = 1
		Fenmu = 1
		for j in range(len(X)):
			if i!=j:
				Fenzi = Fenzi * (x - X[j])
				Fenmu = Fenmu * (X[i] - X[j])
		L.append(Fenzi/Fenmu)
	# 求fx
	SUM = 0
	for i in range(len(Y)):
		SUM = SUM + Y[i] * L[i]
	print('f({0})={1}'.format(x,SUM))

if __name__ == '__main__':
	func(float(input('请输入x,以求Fx: ')))
