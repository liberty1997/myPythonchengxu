#!/bin/python3
# -*- coding: UTF-8 -*-
import math
f = open(r'Jacobi_data.txt')
lines = f.readlines()
b = []
a = []
for line in lines:
	line = line.split()
	aa = []
	for i in range(len(line)):
		if i == len(line)-1:
			b.append(float(line[i]))
		else:
			aa.append(float(line[i]))
	a.append(aa)
f.close()

def Jacobi(*x):
	x = list(x)
	c = x.pop()
	print('t={} {}'.format(c,x))
	xx = []
	Fan1 = 0
	for i in x:
		Fan1 += i**2
	for i in range(len(x)):
		t = 0
		for j in range(len(a)):
			if j!= i:
				t += (a[i][j] * x[j])
		xx.append((b[i] - t) / a[i][i])
	c += 1
	Fan2 = 0
	for i in xx:
		Fan2 += i**2
	if math.fabs(math.sqrt(Fan2) - math.sqrt(Fan1)) < 0.5*(10**(-2)):
		print('t={}\n{}'.format(c,xx))
	else:
		xx.append(c)
		Jacobi(*xx)

if __name__ == '__main__':
	Jacobi(0,0,0,0)
