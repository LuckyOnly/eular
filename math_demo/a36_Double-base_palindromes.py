# coding:utf-8


def palindromes_method(num):
    L=[]
    for i in str(num):
        L.append(i)
    a=0
    b=len(L)-1
    while a <= b:
        if L[a]!=L[b]:
            return False
        a+=1
        b-=1
    return True


def double_method(num):
    sum = 0
    for i in range(1,num+1):
        if palindromes_method(bin(i)[2:]) and palindromes_method(i):
            sum+=i
    return sum

print double_method(1000000)
