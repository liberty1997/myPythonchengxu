#!/bin/python3
# -*- coding: UTF-8 -*-
import math
f = open(r'GaussSeidel_data.txt')
lines = f.readlines()
b = []
a = []
for line in lines:
	line = line.split()
	a1 = []
	for i in range(len(line)):
		if i == (len(line)-1):
			b.append(float(line[i]))
		else:
			a1.append(float(line[i]))
	a.append(a1)

def Gauss_Seidel(*x):
	x = list(x)
	c = x.pop()
	print('t={} {}'.format(c,x))
	Fan1 = 0
	for i in x:
		Fan1 += i**2
	for i in range(len(x)):
		t = 0
		for j in range(len(a)):
			if j!= i:
				t += (a[i][j] * x[j])
		x[i] = ((b[i] - t) / a[i][i])
	c += 1
	Fan2 = 0
	for i in x:
		Fan2 += i**2
	if math.fabs(math.sqrt(Fan2) - math.sqrt(Fan1)) < 0.5 * 10**(-2):
		print('t={}\n{}'.format(c,x))
	else:
		x.append(c)
		Gauss_Seidel(*x)

if __name__ == '__main__':
	Gauss_Seidel(0,0,0,0)
