# coding:utf-8


def digit_method(num):
    token =[]
    L=[]
    n=1
    while len(token)<9:
        tmp = num*n
        for i in str(tmp):
            if i in token or i == "0":
                return 0
            token.append(i)
        L.append(tmp)
        n+=1
    return L

def match_method(L):
    strings = ""
    for i in L:
        strings+=str(i)
    return int(strings)

def pandigital_method(num):
    i = 9
    max_num = 0
    while i<num:
        if digit_method(i)!=0:
            n = match_method(digit_method(i))
            if n>max_num:
                max_num = n
        i+=1
    return max_num

print pandigital_method(10000)


