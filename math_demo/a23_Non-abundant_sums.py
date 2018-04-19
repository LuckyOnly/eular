# coding:utf-8
from  a21_Amicable_numbers import *
token={1:{1:1}}
L=[]
def abundant_num(num):
    i = 2
    while i <=num:
        if ini(i)>i and i not in L:
            L.append(i)
        i+=1
    return L

def result(num):
    i = 1
    tmp = 0
    while i <= num:
        if is_right(i):
            tmp +=i
        i+=1
    return tmp


def is_right(i):
    j = 0
    while j < len(L):
        if i in L:
            return False
        k = i - L[j]
        if k < 0:
            return True
        else:
            if k in L:
                return False
            else:
                j += 1

def sumOfNonAbundant(num):
    sum = 0
    result1 = abundant_num(num)
    flag = [False for i in range(num)]
    l = len(result1)
    for i in range(l):
        for j in range(i,l):
            if result1[i]+result1[j]<num:#
                flag[result1[i]+result1[j]]=True
    for i in range(num):
        if flag[i]==False:
            sum += i
    return sum


def sum(num):
    i = 1
    tmp = 0
    while i<=num:
        tmp +=i
        i+=1
    return tmp
#4178876
# abundant_num(28123)
# print result(28123)
print sum(28123)
print sumOfNonAbundant(28124)
