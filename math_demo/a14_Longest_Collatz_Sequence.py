# coding:utf-8
# 判断是否未偶数
def is_even(num):
    if num % 2 ==0:
        return True
    return False

# 奇数 n/2
# 偶数 3n+1

def calculate(num):
    # tmp = 1
    if is_even(num):
        num = num / 2

    else:
        num = 3 * num + 1
    # tmp +=1
    return num

def method(num):
    max = 0
    i = num
    while i>1:
        counter = 0
        tmp=i
        while calculate(tmp)!=1:
            counter += 1
            tmp = calculate(tmp)
        if counter>max:
            max=counter+1
            value = i
        i-=1
    return max, value

def test():
    max = 0
    i=13
    counter = 0
    while calculate(i) != 1:
        counter += 1
        i = calculate(i)
    if counter>max:
        max=counter+1
    return max

print method(1000000)