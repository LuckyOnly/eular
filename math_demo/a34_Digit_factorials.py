# coding:utf-8
token={0:1,1:1}
def fac_method(num):
    if num in token:
        return token[num]
    token[num] = fac_method(num-1)*num
    return token[num]

def digit_method4():
    t= 0
    for i in range(100,50000):
        num = i
        sum = 0
        while num!=0:
            a = num%10
            sum+=fac_method(a)
            num = num /10
        if sum==i:
            t+=i
    return t

print digit_method4()

