# coding:utf-8

from palindromic_method import is_pal


def reverse_num(num):
    s = str(num)
    tmp = 0
    i = 0
    while i<len(s):
        tmp += int(s[i])*10**i
        i+=1
    return tmp


def sum_method(num):
    tmp = num + reverse_num(num)
    return tmp


def count_method(num):
    sum_L =set()
    sum_S =set()
    for index in xrange(1,num):
        L=set()
        i = 0
        tmp = index
        if index not in sum_L and index not in  sum_S:
            while i < 50:
                if tmp<num:
                    L.add(tmp)
                tmp = sum_method(tmp)
                if is_pal(tmp):
                    # print tmp
                    sum_L |=L
                    break
                i += 1
            if i == 50:
                sum_S|=L
    return len(sum_L),len(sum_S),len(sum_L)+len(sum_S),max(sum_L)

print count_method(10000)

