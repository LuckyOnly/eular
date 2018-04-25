# coding:utf-8
import math


def is_prime(num):
    a = int(math.sqrt(num))
    i = 2
    while i<=a:
        if num % i == 0:
            return False
        i+=1
    return True

from itertools import permutations
def pandigital_method(n):
    i = 1
    L=[]
    while i<=n:
        L.append(i)
        i+=1
    S = list(permutations(L,n))
    T = method_n_digit(S, n)
    num = max_prime(T)
    return num


def method_n_digit(S, n):
    T = []
    for j in S:
        m = 0
        a = 0
        while m < n:
            a += j[m] * 10 ** (n - m - 1)
            m += 1
        T.append(a)
    return T


def max_prime(L):
    L.sort(reverse=True)
    for i in L:
        if is_prime(i):
            return i
    return 0


def max_method():
    n= 9
    while n>=4:
        a = pandigital_method(n)
        if a!=0:
            return a
        n-=1
    return 0

print max_method()


