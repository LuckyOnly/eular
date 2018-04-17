# coding:utf-8
token = {1:{1:1}}
def cnt(num):
    if num in token:
        dvalue = token[num]

    else:
        or_num = num
        dvalue=dict()
        for start in xrange(2,num+1):
            if not num % start:
                dvalue[start]=1
                num = num /start
                break
        if num == 1:
            token[or_num]=dvalue
            return dvalue
        dlist = cnt(num)
        for key,value in dlist.iteritems():
            dvalue[key]=value+dvalue.get(key,0)
        token[or_num]=dvalue

    return dvalue

def cnt1(num):
    if num in token:
        dvalue = token[num]
    else:
        or_num = num
        dvalue=dict()
        t=1
        start = 1
        while start <= t:
            if not or_num % start:
                dvalue[start]=1
                t = num /start
                dvalue[t]=1
            start+=1
        if num == 1:
            token[or_num]=dvalue
            return dvalue
        token[or_num]=dvalue
    return dvalue

import operator
def sum(dvalue):

    tmp = reduce(operator.add,dvalue.keys())
    return tmp

def condition_method(num):
    i=0
    L=[]
    for i in range(2,num+1):
        b=ini(i)
        if ini(b)==i and b != i:
            if i not in L:
                L.append(i)
            if b not in L and b < num:
                L.append(b)

    return reduce(operator.add,L)
def ini(num):
    b= cnt1(num)
    return sum(b)-num
print condition_method(10000)