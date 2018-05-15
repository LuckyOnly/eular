# coding:utf-8


def digit_method(num):
    return len(str(num))
import math
def others():
    counter = 0
    for n in range(1, 22):
        counter += 10 - int(math.ceil(10 ** ((n - 1)*1.0 / n)))
    return counter
def counter_num():
    n_th = 1
    count = 0
    while n_th<=100:
        n_digit = 1
        while n_digit<10:
            num = n_digit ** n_th
            n = digit_method(num)
            if n == n_th:
                count += 1
                break
            else:
                n_digit+=1

        n_th +=1
    return count
def tes():
    n= 2
    while True:
        if digit_method(2**n)> n:
            print n
            break
        n+=1
print others()

