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
