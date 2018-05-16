# coding:utf-8
import math
# S = 23
# d = 1
# m = 0
# a = 0
def property_method(s,m,d):
    a1 = int((math.sqrt(s)+m)/d)
    m1 = a1*d-m
    d1 = (s-m1**2)/d
    return a1,m1,d1
def cycly_method(num):
    L = []
    m,d = 0,1
    a, m, d = property_method(num, m, d)
    while True:
        if d ==0:
            break
        a1,m,d = property_method(num,m,d)
        if a1==a*2:
            L.append(a1)
            break
        L.append(a1)
    return len(L)
def count_method(num):
    i = 2
    count = 0
    while i<num:
        if cycly_method(i)%2!=0:
            count +=1
        i+=1
    return count

print count_method(10000)


