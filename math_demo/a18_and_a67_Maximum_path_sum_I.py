# coding:utf-8
from file import *
token = {}
strings = ""
import sys
with open(sys.path[0]+r"\file\triangle_100.txt") as f:
    for line in f:
        strings += line.strip()+" "
L = strings.split(" ")


def triangle(L,row):
    i = 0
    j = 1
    while j <= row:
        s1 = []
        while i<len(L) and len(s1)<j :
            if L[i] != " ":
                s1.append(int(L[i]))
            token[j]=s1
            i+=1
        j +=1
    return token


def result1(row):
    j = 0
    i = row -1
    while j<i:
        s1 = token[i][j]+token[i+1][j]
        s2 = token[i][j] + token[i + 1][j+1]
        token[i][j] = max(s1, s2)
        j+=1
    return token


def circle(row):
    while row >1:
        result1(row)
        row-=1
    return token[1][0]

row = 100
triangle(L,row)
print circle(row)
