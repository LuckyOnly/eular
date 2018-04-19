# coding:utf-8
import operator
def data_id():
    L = [0,1,2,3,4,5,6,7,8,9]
    S = []
    a = len(L)# 代表需要确认的值
    # counter = 1
    t = 1000000  # 代表需要确认的值
    while a > 0:
        counter = 1
        num = factorial(a)
        eve_num = num/a
        p = eve_num
        while  p < t:
            counter+=1
            p = counter*eve_num
        S.append(L[counter-1])
        L.remove(L[counter-1])
        t = t - eve_num*(counter-1)
        a=len(L)
    return S
def factorial(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i
    return sum
def splice_med(S):
    strings =""
    for i in S:
        strings+=str(i)
    return strings
print splice_med(data_id())
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# L.remove(2)
# print L