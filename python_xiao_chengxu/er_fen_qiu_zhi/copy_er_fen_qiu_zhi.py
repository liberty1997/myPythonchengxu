#!/bin/python
# -*- coding: UTF-8 -*-

import math

def fangchengshi(x) :
    F = x**3 + 4*(x**2) -10
    #F = math.exp(x) + 10 * x - 2
    return F

def func(low,high) :
    l = fangchengshi(low)
    h = fangchengshi(high)
    mm = (low + high ) / 2.0
    m = fangchengshi(mm)
    print("low = %.8f" % low)
    print("high = %.8f" % high)
    print("mm = %.8f" % mm)
    print("l = %.8f" % l)
    print("h = %.8f" % h)
    print("m = %.8f" % m)
    #if round(mm,8) - mm != 0.0 :
    if (h-l)/2.0 < (0.5*0.001) :
        print("Ans : %.8f" % mm)
        return
    elif l * m < 0 :
        func(low,mm)
    elif m * h < 0 :
        func(mm,high)

if __name__ == '__main__' :
    func(1.0,2.0)
