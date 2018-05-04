# coding:utf-8
token={0:1,1:1}


def factor_method(num):
    if num in token:
        return token[num]
    token[num] = num * factor_method(num-1)
    return token[num]


def is_odd(num):
    if num % 2==0:
        return False
    return True


def count_method(num,value):
    i = 1
    while i <= int(num/2):
        if factor_method(num)/(factor_method(i)*factor_method(num-i))>value:
            if is_odd(num):
                return (int(num/2)-i+1)*2
            else:
                return (int(num/2)-i+1)*2-1
        i+=1
    return 0

def combinator_method():
    i = 1
    counter = 0
    while i<=100:
        counter+=count_method(i,1000000)
        i+=1
    print counter
combinator_method()
# print factor_method(5)/(factor_method(0)*factor_method(5-0))
# print factor_method(5)/(factor_method(1)*factor_method(5-1))
# print factor_method(5)/(factor_method(2)*factor_method(5-2))
# print factor_method(5)/(factor_method(3)*factor_method(5-3))
# print factor_method(5)/(factor_method(4)*factor_method(5-4))
# print factor_method(5)/(factor_method(5)*factor_method(5-5))