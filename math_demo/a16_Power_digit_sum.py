# coding:utf-8

def sum(num):
    L = str(2**num)
    i = 0
    sum = 0
    while i < len(L):
        sum+=int(L[i])
        i+=1
    return sum

print sum(1000)