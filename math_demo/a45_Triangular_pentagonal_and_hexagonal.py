# coding:utf-8

token ={}
def pentagon_method(n):
    if n in token:
        return token[n]
    a = n*(3*n-1)/2
    token[n]=a
    return token[n]

cookie={}
def hexagonal_method(n):
    if n in cookie:
        return cookie[n]
    a = n*(2*n-1)
    cookie[n]=a
    return cookie[n]

rmp={}
def triangular_method(n):
    if n in rmp:
        return rmp[n]
    a = n*(n+1)/2
    rmp[n]=a
    return rmp[n]

import math
def is_true(m):
    p = int(math.sqrt(24*m+1)+1)/6
    q = int(math.sqrt(8*m+1)+1)/4
    if pentagon_method(p)==m and hexagonal_method(q) == m:
        return True
    return False

def next_method():
    i = 286
    while True:
        m = triangular_method(i)
        if is_true(m):
            return m
        i+=1

print next_method()