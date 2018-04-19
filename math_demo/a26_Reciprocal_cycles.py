# coding:utf-8


def fermat_theorem(num):
    for a in range(1,num):
        if 10**a%num == 1:
            return a
    return 0


def result():
    longest = 0
    tmp = 0
    for i in range(2,1001):
        num = fermat_theorem(i)
        if num>longest:
            longest = num
            tmp = i
    return longest,tmp

print fermat_theorem(6)
