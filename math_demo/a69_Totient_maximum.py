# coding:utf-8

def gcd(a,b):
    while b !=0 and b!= 1:
        a,b = b,a%b
    if b == 0:
        return a
    if b == 1:
        return b


def fi_func(num):
    count = 0
    for i in xrange(1, num):
        if gcd(num, i) == 1:
            count += 1
    return num*1.0/count
# max_count = 3
# for i in xrange(2,1000001):
#     if fi_func(i)>max_count:
#         max_count=fi_func(i)
# print max_count

from Euler import prime_sieve


def result_n():
    count = 1
    L =  prime_sieve(23)
    t = 1
    for i in L:
        if count <1000000:
            count *=i
            t = i
    return count/t
print result_n()




