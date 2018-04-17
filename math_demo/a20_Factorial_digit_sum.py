# coding:utf-8

def factorial_method(num):
    if num == 1:
        return 1
    if num > 1:
        return factorial_method(num-1)*num

def sum(strings):
    i = 0
    total = 0
    while i < len(strings):
        total+= int(strings[i])
        i +=1
    return total

print sum(str(factorial_method(100)))