# coding:utf-8

def is_even(num):
    if num % 2== 0:
        return True
    return False

token = {1:1,2:2}
def fibonnacci(num):
    if num == 1 or num == 2:
        return token[num]
    if num in token:
        return token[num]
    value = fibonnacci(num-2)+fibonnacci(num-1)
    if num not in token:
        token[num] = value
    return value

def sum(num):
    i = 1
    tmp = 0
    while fibonnacci(i)<num:
        t = fibonnacci(i)
        if is_even(t):
            tmp += t
        i+=1
    return tmp
print sum(4000000)