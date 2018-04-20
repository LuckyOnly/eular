# coding:utf-8

def input_num1(num):
    i= 0
    sum = 0
    while i <num:
        i += 1
        sum +=i
    return sum

known = {1: 1}


def input_num(indice):
    if indice in known:
        return known[indice]
    else:
        temp = input_num(indice - 1) + indice
        known[indice] = temp
        return temp
import b12_other
def result(num):
    start =1
    cn = 1
    sum = 1
    while cn<num:
        start+=1
        sum =input_num(start)
        cn = reduce(operator.mul, [x + 1 for x in b12_other.cnt(sum).values()])
    return sum

def factors(num):
    L = construction_prime(2000)
    S=[]
    i =0
    while i < len(L):
        counter = method_counter(num,L[i])
        S.append(counter+1)
        i+=1
    return S
token ={2:{2:1},3:{3:1},1:{1:1}}
def fast_method(num):
    if num in token:
        dvalue = token[num]
    else:
        or_num = num
        dvalue = dict()
        for start in range(2,num+1):
            if not num % start:
                dvalue[start]=1
                num /=start
                break
        if num == 1:
            token[or_num] = dvalue
            return dvalue
        dlist = fast_method(num)
        for key,value in dlist.iteritems():
            dvalue[key]=dvalue.get(key,0)+ value
        token[or_num] = dvalue
    return dvalue


import operator
def index2(num):
    return reduce(operator.mul,[x+1 for x in fast_method(num).values() ])
def index(S):
    return reduce(operator.mul,S)
    # i = 0
    # contructor_l = 1
    # while i < len(S):
    #     if S[i]!=1:
    #         contructor_l *=S[i]
    #     i +=1
    # return contructor_l

def method_counter(num,i):
    counter = 0
    tmp = num
    while tmp % i == 0:
        counter += 1
        tmp /= i
    return counter


def construction_prime(num):
    i = 0
    j=2
    L=[]
    while i < num:
        if is_prime(j):
            L.append(j)
            i+=1
        j+=1
    return L


import  math
def is_prime(num):
    i=2
    while i <= int(math.sqrt(num)):
        if num % i == 0:
            return False
        i+=1
    return True


# print fast_method(100)
# print index2(100)
print result(500)
# S = [2, 3, 1, 1]
# print index([1,2,3])
# print index(S)
# print construction_prime(13)