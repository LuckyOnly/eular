# coding:utf-8
from itertools import permutations


def pandigital_method(n):
    i = 0
    L=[]
    while i<n:
        L.append(i)
        i+=1
    S = list(permutations(L,n))
    return S


def sub_string_method():
    S = pandigital_method(10)
    sum = 0
    for j in S:
        if j[0]!=0 and three_partial(j):
            sum += method_n_digit(j)
    return sum

def method_n_digit(S):
    m = 0
    a = 0
    n = len(S)
    while m < n:
        for j in S:

            a += j * 10 ** (n - m - 1)
            m += 1
    return a

def three_partial(j):
    L = [2, 3, 5, 7, 11, 13, 17]
    t = 0
    m = 1
    while t < len(L):
        a = 0
        counter = 0
        while counter < 3:
            a += j[m] * 10 ** (3 - counter - 1)
            m += 1
            counter += 1
        if a%L[t] != 0:
            return False
        m = m-2
        t+=1
    return True

# print three_partial((1,4,0,6,3,5,7,2,9,8))
# print method_n_digit((1,4,0,6,3,5,7,2,9,8))

print sub_string_method()