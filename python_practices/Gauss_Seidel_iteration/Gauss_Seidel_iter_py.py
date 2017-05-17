#!/bin/python3
# -*- coding: UTF-8 -*-

import math

func1 = lambda a,b:(9-a+2*b)/8
func2 = lambda a,b:(19-3*a-b)/10
func3 = lambda a,b:(72-5*a+2*b)/20

def Gauss_Seidel(x1,x2,x3,t):
	print("x1= {} x2= {} x3= {}".format(x1,x2,x3))
	x11 = func1(x2,x3)
	x22 = func2(x11,x3)
	x33 = func3(x11,x22)
	t = t + 1
	Fan1 = math.sqrt(x1**2+x2**2+x3**2)
	Fan2 = math.sqrt(x11**2+x22**2+x33**2)
	if math.fabs(Fan2 - Fan1) < 0.5*(10**(-2)):
		print("x1= ",x11," x2= ",x22," x3= ",x33)
		print("t=", t)
		print("x1= %.2f, x2= %.2f, x3= %.2f" % (x1,x2,x3))
		return
	else:
		Gauss_Seidel(x11,x22,x33,t)

if __name__ == '__main__':
	Gauss_Seidel(0,0,0,0)
