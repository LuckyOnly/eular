# coding:utf-8


def count_sum(num):
    tmp = 0
    for i in num:
        tmp += int(i)
    return tmp

def power_est(a,b):
    return str(a**b)

def ini():
    max_num = 0
    for i in range(1,100):
        for j in range(1,100):
            num = count_sum(power_est(i,j))
            if max_num < num:
                max_num=num
    return max_num


print ini()