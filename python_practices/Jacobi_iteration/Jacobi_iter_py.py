#!/bin/python3
# -*- coding: UTF-8 -*-

import math

def func1(a,b):
	return ((9-a+2*b)/8)
def func2(a,b):
	return ((19-3*a-b)/10)
def func3(a,b):
	return ((72-5*a+2*b)/20)

def Jacobi(x1,x2,x3,t):
	Fan1 = math.sqrt(x1**2+x2**2+x3**2)
	x11 = func1(x2,x3)
	x22 = func2(x1,x3)
	x33 = func3(x1,x2)
	t = t + 1
	Fan2 = math.sqrt(x11**2+x22**2+x33**2)
	if math.fabs(Fan2 - Fan1) < 0.5*(10**(-2)): # 范数控制精度
		print("t= ",t)
		print("x1= %.2f, x2= %.2f, x3= %.2f" % (x1,x2,x3))
		return
	else:
		Jacobi(x11,x22,x33,t)

if __name__ == '__main__':
	Jacobi(0,0,0,0)
