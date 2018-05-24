# coding:utf-8
from Euler import prime_sieve
from math import *
L = 10 ** 7
primes = prime_sieve(int(1.30 * sqrt(L)))
del primes[:int(0.6 * len(primes))]
def match(i, j):
    k1 = sorted(list(str((i-1)*(j-1))))
    k2 = sorted(list(str(i*j)))
    return k1==k2

min_n = 9999999
for i in primes:
    for j in primes:
        if j>i:
            if match(i, j) and i*j<10**7:
                t = i * j * 1.0 / (i - 1) / (j - 1)
                if min_n > t:
                    min_n =t
                    idx = i*j
print idx
