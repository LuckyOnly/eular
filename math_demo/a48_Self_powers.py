# coding:utf-8

def power_method(num):
    s = str(num**num)
    if len(s) >= 10:
        return int(s[-10:])
    return int(s)

def method(num):
    i=1
    sum = 0
    while i<= num:
        print i,power_method(i)
        sum+=power_method(i)
        t = str(sum)
        if len(t) >= 10:
            sum = int(t[-10:])
        i+=1
    return sum
print method(1000)