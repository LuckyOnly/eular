# coding:utf-8
import math


def is_prime(num):
    if num < 0:
        num = abs(num)
    size = int(math.sqrt(num))
    i = 2
    while i <= size:
        if num % i == 0:
            return False
        i+=1
    return True

def all_prime(num):
    L = []
    for i in range(-num,num):
        if is_prime(i):
            L.append(i)
    L.remove(0)
    L.remove(1)
    L.remove(-1)

    return L
token={0:0}


def find_a():
    L= all_prime(1001)
    size = 0
    for j in L:
        for i in range(-j, 1000):
            n = get_size(i, j)
            if size<n:
                size=n
                token[n]=i*j
    return token


def get_size(i, j):
    n = 1
    c = n ** n + i * n + j
    while is_prime(c):
        n += 1
        c = n ** 2 + i * n + j
    return n


# print get_size(1,41)
print find_a()


