#!/bin/python3
# -*- coding: UTF-8 -*-
f = open(r'NewtonChazhi_data.txt')
lines = f.readlines()
X = []
Y = []
for line in lines:
	line = line.split()
	line = list(map(float,line))
	X.append(line[0])
	Y.append(line[1])
f.close()

def Chashang(n):
	C = 0
	for i in range(0,n+1):
		t = 1
		for j in range(0,n+1):
			if i != j:
				t = t * (X[i]-X[j])
		C = C + (Y[i] / t)
	return C;

def func(x):
	N = Y[0]
	for i in range(1,len(X)):
		t = 1
		for j in range(0,i):
			t = t * (x-X[j])
		N = N + Chashang(i) * t
	print("N(x)=N({0})={1}".format(x,N))

if __name__ == '__main__':
	func(float(input('请输入x: 如0.596\n')))
