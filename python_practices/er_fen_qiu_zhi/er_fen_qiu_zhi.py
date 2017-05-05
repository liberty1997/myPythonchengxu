#!/bin/python3
# -*- coding: UTF-8 -*-

#import math

def fangchengshi(x):
    F = x**3 + 4*(x**2) - 10
    return F

def func(low,high,n):
    n = n + 1
    l = fangchengshi(low)
    h = fangchengshi(high)
    mm = (low + high ) / 2
    m = fangchengshi(mm)
    print("mm= ", mm)
    # 符合精度,到达递归出口
    if m == 0 or low==high or (high-low) / 2 < (0.5 * 10**(-5)):
        print("Ans :%.5f" % mm)
        print("次数:", n)
        return
    # 左半
    if l * m < 0:
        func(low,mm,n)
    # 右半
    if m * h < 0:
        func(mm,high,n)

if __name__ == '__main__':
    func(1,2,0)
