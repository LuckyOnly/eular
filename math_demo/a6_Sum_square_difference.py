# coding:utf-8

def square(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum*sum

def count(num):
    sum =0
    for i in range(1, num+1):
        sum += i*i
    return sum

print square(100)-count(100)