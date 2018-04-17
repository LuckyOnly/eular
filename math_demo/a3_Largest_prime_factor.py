# coding:utf-8
import math


def value(num):
    return math.sqrt(num)


def prime(num):
    len = int(math.sqrt(num))
    i=2
    while i <= len:
        if num%i==0:
            return False
        i=i+1
    return True

def max_prime(num):
    j = int(value(num))
    # j=30
    while j>2:
        j-=1
        if prime(j) and  num%j==0:
            return j
    return num
def change_prime(num,value):
    j = num/value
    while j>value:
        j-=1
        if prime(j) and  num%j==0:
            return j
    return num
print change_prime(600851475143,6857)