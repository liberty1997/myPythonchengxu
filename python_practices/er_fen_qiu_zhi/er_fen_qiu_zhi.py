#!/bin/python
# -*- coding: UTF-8 -*-

import math

def fangchengshi(x) :
    F = math.exp(x) + 10 * x - 2
    return F

def func(low,high) :
    l = fangchengshi(low)
    h = fangchengshi(high)
    mm = (low + high ) / 2.0
    m = fangchengshi(mm)
    if (h-l) / 2.0 < (0.5 * 10**(-3)) :
#    if round(mm,3) - mm != 0.0 :
        print("Ans : %.3f" % mm)
        return
    elif l * m < 0 :
        func(low,mm)
    elif m * h < 0 :
        func(mm,high)

if __name__ == '__main__' :
    func(0.0,1.0)
