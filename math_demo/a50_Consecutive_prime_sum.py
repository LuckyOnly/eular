# coding:utf-8
from  prime_distinct import is_prime

L=[]
def construct_primes():
    for i in range(2,100000):
        if is_prime(i):
            L.append(i)


def sum_prime(num):
    i = 0
    sum = 0
    while sum < num:
        sum+=L[i]
        i+=1
    return i-2,sum-L[i-1]

import operator
def sum_count(num):
    return reduce(operator.add,L[:num])


token={}
def method_forward(i,sum):
    tmp =sum
    j =0
    p = 0
    while tmp:
        if is_prime(tmp):
            if i-j>p:
                p =i-j
                token[p]=tmp
            tmp -= L[j]
            j += 1
        else:
            tmp -= L[j]
            j += 1
    return token[p],p

def method_back(i,sum):
    tmp =sum
    p = 0
    while tmp:
        if is_prime(tmp):
            if i>p:
                p = i
                token[p] = tmp
            tmp -= L[i]
            i -= 1
        else:
            tmp-=L[i]
            i-=1
    return token[p], p

def method():
    construct_primes()
    i,num = sum_prime(1000000)
    a,m = method_back(i,num)
    b,n = method_forward(i,num)
    print token[max(m,n)]

#
# # construct_primes()
# print sum_count(8)
# print method_forward(24,963)
method()
# method_back()