# coding:utf-8
import math
def is_prime(num):
    if num==0 or num ==1:
        return False
    size = int(math.sqrt(num))
    i=2
    while i<= size:
        if num % i == 0:
            return False
        i+=1
    return True

def check(num):
    mul =1
    while mul<num:
        mul*=10
    mul/=10
    tmp = num
    while True:
        if tmp%10==0:
            return False
        tmp = tmp/10+tmp%10*mul
        if not is_prime(tmp):
            return False
        if tmp==num:
            break
    return True


def check2(num):
    tmp = num
    while tmp!=0:
        if not is_prime(tmp):
            return False
        tmp = tmp / 10
    return True

def check3(num):
    mul =1
    while mul<num:
        mul*=10
    mul/=10
    tmp = num % mul
    while mul!=1:
        if not is_prime(tmp):
            return False
        mul/=10
        tmp = tmp % mul
    return True


def trunc_method():
    count = 0
    i =10
    sum=0
    while count<11:
        if check2(i) and check3(i):
            print i
            count+=1
            sum+=i
        i+=1
    return sum

print trunc_method()

















