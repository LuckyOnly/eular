# coding:utf-8

import operator


def add_method(L):
    return reduce(operator.add,L)

def paths(num):
    L=[]
    if num == 1:
        L.append(1)
        return L
    L.append(add_method(paths(num-1))*2)
    i = 0
    while i<num-1:
        L.append(add_method(paths(num-1)[i:]))
        i += 1
    # L.append(add_method(paths(num-1)[1:]))
    print L
    return L
token ={2:[2,1],1:[1]}
def paths1(num):
    L=[]
    if num in token:
        return token[num]

    L.append(add_method(paths1(num-1))*2)
    i = 0
    while i<num-1:
        L.append(add_method(paths1(num-1)[i:]))
        i += 1
    # L.append(add_method(paths(num-1)[1:]))
    if num not in token:
        token[num]=L
    return L
# print paths1(20),token
print add_method(paths1(20))*2
token ={10:[48900, 24450, 11500, 5025, 2006, 715, 220, 55, 10, 1,112],12:[48900, 24450, 11500, 5025, 2006, 715, 220, 55, 10, 1]}
# for key,value in token.iteritems():
#     if key == 10:
#         L=value
# if 10 in token:
#     L = token[10]
# token[13]=[1444]
# print token[13]