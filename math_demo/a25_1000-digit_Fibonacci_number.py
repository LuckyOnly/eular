# coding:utf-8


def digits_num(num):
    return len(str(num))

token={1:1,2:1}
def fibonacci_med(num):
    if num in token:
        return token[num]
    return fibonacci_med(num-1)+fibonacci_med(num-2)

def result(num):
    i = 1
    while digits_num(fibonacci_med(i))< num:
        token[i]=fibonacci_med(i)
        i += 1
    return i

print result(1000)
