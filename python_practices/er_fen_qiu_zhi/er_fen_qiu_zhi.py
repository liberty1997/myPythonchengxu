#!/bin/python
# -*- coding: UTF-8 -*-

#import math

def fangchengshi(x):
    F = x**3 + 4*(x**2) - 10
    #F = x**2 - 2*x + 1
    #F = math.exp(x)+10*x-2
    return F

def func(low,high,n):
    n = n + 1
    l = fangchengshi(low)
    h = fangchengshi(high)
    mm = (low + high ) * 0.5
    m = fangchengshi(mm)
    #print("mm = %.8f" % mm)
    # 符合精度,到达递归出口
    if (m ==0 ) or (((h-l) * 0.5) < (0.5 * 10**(-5))):
        print("Ans : ",mm)
        print("次数: %d" % n)
        return
    # 左半
    if l * m < 0:
        func(low,mm,n)
    # 右半
    elif m * h < 0:
        func(mm,high,n)

if __name__ == '__main__':
    func(1,2,0)
