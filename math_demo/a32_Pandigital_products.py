# coding:utf-8
cookie = []


def match(multiplicand,multiplier,product):
    token=[]
    if is_repeat(multiplicand,token) and is_repeat(multiplier,token) and is_repeat(product,token):
        # cookie.append(product)
        if len(token)==9:
            return product
    return 0


def is_repeat(multiplicand,token):

    for i in str(multiplicand):
        if i == "0":
            return False
        if i in token:
            return False
        token.append(i)
    return True


def pro_method1():
    # L = [1,2,3,4,5,6,7,8,9]
    S =set()
    for i in range(1,10):
        for j in range(2,10):
            if j != i:
                m = i*10+j
            for a in range(1,10):
                for b in range(1,10):
                    for c in range(2,10):
                        if a != i and a!=j:
                            if b != i and b!=j and b!=a:
                                if c != i and c!=j and c!=a and c!= b:
                                    n = a*100+b*10+c
                                    p = m * n
                                    t = match(m,n,p)
                                    if t!=0:
                                        S.add(t)
                                        print m,n,p
    return S

def pro_method2():
    # L = [1,2,3,4,5,6,7,8,9]
    S =set()
    for i in range(2,10):
        m = i
        for j in range(1,10):
            for a in range(1,10):
                for b in range(1,10):
                    for c in range(2,10):
                        if j != i:
                            if a != i and a!=j:
                                if b != i and b!=j and b!=a:
                                    if c != i and c!=j and c!=a and c!= b:
                                        n = j*1000+a*100+b*10+c
                                        p = m * n
                                        t = match(m,n,p)
                                        if t!=0:
                                            S.add(t)
                                            print m,n,p
    return S

def pro_method3():
    # L = [1,2,3,4,5,6,7,8,9]
    S =set()
    for i in range(2,10):
        m = i
        for a in range(1, 10):
            for b in range(1, 10):
                for c in range(2, 10):
                    if a != i :
                        if b != i and b != a:
                            if c != i and  c != a and c != b:
                                n = a * 100 + b * 10 + c
                                p = m * n
                                t = match(m, n, p)
                                if t != 0:
                                    S.add(t)
                                    print m, n, p
    return S

import operator
print 41566+14804

print reduce(operator.add,pro_method1())+ reduce(operator.add,pro_method2())

# print pro_method3()

# token =[]
# print is_repeat(1001,token)