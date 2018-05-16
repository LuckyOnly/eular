# coding:utf-8
import math
from fractions import Fraction
def property_method(s,m,d):
    a1 = int((math.sqrt(s)+m)/d)
    m1 = a1*d-m
    d1 = (s-m1**2)/d
    print a1,m1,d1
    a = str(a1+Fraction(1,s))
    return a

token={1:1}


def fraction_method(num):
    i = 1
    s = num
    if num in token:
        return token[num]
    if num%3==2:
        token[s] = (num*2)/3+1
        return token[s]
    if i != num:
        num -= 1
        token[s] = 2 + Fraction(1, fraction_method(num))
        return token[s]
    else:
        return 2


def square_method(num):
    # count = 0
    i =1
    while i <= num:
        tmp = 2+Fraction(1,fraction_method(i))
        # if len(str(Fraction(tmp).numerator)) > len(str(Fraction(tmp).denominator)):
        #     count +=1
        i += 1
    return tmp
print square_method(2)
# print property_method(2,0,1)