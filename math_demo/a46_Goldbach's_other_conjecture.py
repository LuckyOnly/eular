# coding:utf-8
import math


def christian_method(num):
    i = 2
    while i<num:
        if is_prime(i):
            j = int(math.sqrt(num/2))
            while j>=1:
                if i+2*j**2 == num:
                    return True
                j-=1
        i+=1
    return False

def method():
    i = 33
    while True:
        if not is_prime(i) and not christian_method(i):
            return i
        i+=2


def is_prime(num):
    i = 2
    a = int(math.sqrt(num))
    while i <= a:
        if num%i == 0:
            return False
        i+=1
    return True


print method()
