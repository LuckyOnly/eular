# coding:utf-8

import math
def prime(num):
    len = int(math.sqrt(num))
    i=2
    while i <= len:
        if num%i==0:
            return False
        i=i+1
    return True

def counter_sum(num):
    counter1 = 2
    sum= 0
    while counter1 < num:
        if prime(counter1):
            sum += counter1
        counter1 += 1
    return sum
print counter_sum(2000000)