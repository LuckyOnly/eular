# coding:utf-8
import operator
import sys
path_name = sys.path[0]+r"\file\p022_names.txt"
strings =""
with open(path_name) as f:
    for line in f:
        strings += line.strip()

L = strings.split(",")
L.sort()

def alphaToNum(strings):
    L=[]
    for i in strings:
        # print ord(i)
        L.append(ord(i)-64)
    return reduce(operator.add,L)


def sum(L):
    # print L
    tmp = 0
    for i in L:
        t = eval(i)
        tmp += counter(t)*alphaToNum(t)
    return tmp


def counter(strs):
    i = 0
    while i <len(L):
        if eval(L[i])==strs:
            return i+1
        i +=1

print sum(L)