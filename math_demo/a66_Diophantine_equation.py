# coding:utf-8
from math import *
def property_method(s,m,d):
    a1 = int((sqrt(s)+m)/d)
    m1 = a1*d-m
    d1 = (s-m1**2)/d
    return a1,m1,d1


def cycly_method(num):
    L = []
    m,d = 0,1
    a, m, d = property_method(num, m, d)
    L.append(a)
    while True:
        if d ==0:
            break
        a1,m,d = property_method(num,m,d)
        if a1==a*2:
            L.append(a1)
            break
        L.append(a1)
    return L

from fractions import Fraction
def result(L):
    size = len(L)
    m = size - 1
    if m%2==0:
        i = size - 2
    else:
        i = size - 1
    while i - 1 >= 0:
        L[i - 1] = L[i - 1] + Fraction(1, L[i])
        i -= 1
    return L[0]

def method(num):
    max_x= 0
    D = 0
    for i in range(5,num+1):
        if sqrt(i) == int(sqrt(i)):
            continue
        a = GetMinx(i)
        if a>max_x:
            max_x=a
            D = i
    return max_x,D

def GetMinx(i):
    for k in GetJianjin(cycly_method(i)):
        if k[1]*k[1]-i*k[0]*k[0] == 1:
            return k[1]


from operator import mod
#生成器，不断返回渐进的连分数
def GetJianjin(LFS):
    idx = 1
    result = [LFS[0]]
    while True:
        a,b = 1,result[idx-1]
        for i in range(idx-2,-1,-1):
            a,b=b,a+b*result[i]
        yield [a,b]
        idx += 1
        result += [LFS[mod(idx-2,len(LFS)-1)+1]]

print method(1000)