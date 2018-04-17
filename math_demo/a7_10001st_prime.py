# coding:utf-8
import math


def is_prime(num):
    i = 2
    while i<=int(math.sqrt(num)):
        if num % i == 0:
            return False
        i += 1
    return True

def prime_num(num):
    counter = 1
    i = 2
    while counter < num:
        i += 1
        if is_prime(i):
            counter+=1
    return i
print prime_num(10001)