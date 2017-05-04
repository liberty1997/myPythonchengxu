#!/bin/python3
# -*- coding: UTF-8 -*-


def fangcheng(x):
    F = x**3 + 4*(x**2) -10
    return F

def yidao(x):
    F = 3*(x**2) + 8*x
    return F

def Newton(x,n):
    n = n + 1
    x1 = x - fangcheng(x) / yidao(x)
    # 符合精度,到达递归出口
    if abs(x1 - x) < 0.5 * 10**(-5):
        print("Ans: ",x)
        print("次数: %d" % (n-1))
        return
    else:
        # 继续迭代
        Newton(x1,n)


if __name__ == '__main__':
    Newton(1.5,0)
