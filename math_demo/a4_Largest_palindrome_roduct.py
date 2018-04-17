# coding:utf-8
import math
def product(a,b):
    return a*b
def prime(num):
    len = int(math.sqrt(num))
    i=2
    while i <= len:
        if num%i==0:
            return False
        i=i+1
    return True
def  palindromic(num):
    strings = str(num)
    j = len(strings)-1
    i=0
    while i <= j:
        if strings[i] != strings[j]:
            return False
        i+=1
        j-=1
    return True

def result():
    L=[]
    for num2 in range(1000,100,-1):
        for num1 in range(1000,100,-1):
            num = num1*num2
            if palindromic(num):
                L.append(num)
            num1-=1
        num2-=1
    return max(L)


print result()