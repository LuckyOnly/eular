# coding:utf-8

def contructor_l(num):
    L=[]
    for i in range(1,num*num+1):
        L.append(i)
    return L
import operator
def splice():
    L = contructor_l(1001)
    size = len(L)
    d=1
    k= 3
    end = L[0]
    sum = 1
    while end != L[size-1]:
        p= 2*d
        t= k*k-1
        a = L[t:t-3*p-1:-p]
        sum +=reduce(operator.add,a)
        d+=1
        k+=2
        end = a[0]
    return sum
print splice()