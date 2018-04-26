# coding:utf-8
import sys
p = sys.path[0]+r'\file\p042_words.txt'
strings=""
with open(p) as f:
    for line in f:
        strings += line.strip()
L=strings.split(',')


import operator
def alphaToNum(strings):
    L=[]
    for i in strings:
        L.append(ord(i)-64)
    return reduce(operator.add,L)


import math
def code_method(num):
    b = 2*num
    a = int(math.sqrt(b))
    if a*(a+1)==b:
        return True
    return False

def count_method():
    count =0
    for i in L:
        if code_method(alphaToNum(eval(i))):
            count +=1
    return count
print count_method()