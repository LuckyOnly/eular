# coding:utf-8

from Euler import sqrt, prime_sieve
# https://en.wikipedia.org/wiki/Chakravala_method

def pell(d):

    p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)

    while k != 1 or y == 0:
        p = k * (p / k + 1) - p
        p = p - int((p - sd) / k) * k

        x = (p * x1 + d * y) / abs(k)
        y = (p * y + x1) / abs(k)
        k = (p * p - d) / k
        x1 = x
    return d,x,y


# L = 1000
# print "Project Euler 66 Solution:", max((pell(d), d) for d in prime_sieve(L))
print pell(61)