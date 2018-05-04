# coding:utf-8
from itertools import permutations


def  match_method(a,b):
    m = str(a)
    n = str(b)
    S1 =[]
    S2 =[]
    for i in m:
        S1.append(i)
    for j in n:
        S2.append(j)
    S1.sort()
    S2.sort()
    return S1 == S2

def permute_method():
    for i in range(125875,1000000):
        count = 2
        while count<=6:
            if match_method(i,count*i):
                count+=1
            else:
                break
        if count ==7:
            return i
print permute_method()


