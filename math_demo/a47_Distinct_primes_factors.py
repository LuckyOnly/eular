# coding:utf-8
import math


def is_prime(num):
    i = 2
    a = int(math.sqrt(num))
    while i <= a:
        if num%i == 0:
            return False
        i+=1
    return True


def method(num,tmp):
    i = 0
    while i<num:
        if not consecutive_method(num,tmp)[1]:
            return False
        tmp+=1
        i+=1
    return True

def factor_method():
    i = 134000
    size = 4
    while True:
        if method(size,i):
            return i
        i+=1
        print i
token={}
def consecutive_method(size,num):
    if num in token:
        if token[num][0]==size:
            return token[num]
    token[num] = [size, False]
    L = set()
    i =2
    tmp =num
    while tmp!=1:
        if is_prime(i):
            while tmp%i==0:
                tmp = tmp/i
                L.add(i)
        i+=1
    if size==len(L):
        token[num]=[size,True]
    return token[num]
# print consecutive_method(3,643)
print factor_method()
# print method(3,643)
