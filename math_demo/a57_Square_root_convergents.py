# coding:utf-8
from fractions import Fraction


def square_method(num):
    count = 0
    i =1
    while i <= num:
        tmp = 1+Fraction(1,fraction_method(i))
        if len(str(Fraction(tmp).numerator)) > len(str(Fraction(tmp).denominator)):
            count +=1
        i += 1
    return count
token={1:2}


def fraction_method(num):
    i = 1
    s = num
    if num in token:
        return token[num]
    if i != num:
        num -= 1
        token[s] = 2 + Fraction(1, fraction_method(num))
        return token[s]
    else:
        return 2


print square_method(1000)