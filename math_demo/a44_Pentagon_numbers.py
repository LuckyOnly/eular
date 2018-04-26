# coding:utf-8


token ={}
def pentagon_method(n):
    if n in token:
        return token[n]
    a = n*(3*n-1)/2
    token[n]=a
    return token[n]

import math
def method(num):
    for i in range(1,num):
        for j in range(i+1,num):
            m = pentagon_method(i) + pentagon_method(j)
            n = pentagon_method(j) - pentagon_method(i)
            if choose_name(n):
                if choose_name(m):
                    return n
    return 0

def test(i,j):
    m = pentagon_method(i) + pentagon_method(j)
    n = pentagon_method(j) - pentagon_method(i)
    if choose_name(n):
        if choose_name(m):
            return n


def choose_name(m):
    # p = int(math.sqrt(m+1))+1
    # q = int(math.sqrt(2 * m / 3))-1
    # while q <= p:
    q=int(math.sqrt(24*m+1)+1)/6
    if pentagon_method(q) == m:
            return True
        # q += 1
    return False

print method(2200)
# print test(1020,2167)
# print choose_name(48)