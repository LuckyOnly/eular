# coding:utf-8
token={}
import operator
def result():
    for k in range(0,10):
        for l in range(0,10):
            for i in range(0,10):
                for j in range(0,10):
                    for p in range(0,10):
                        for q in range(0,10):
                            a =k*10**5+l*10**4+i*10**3+j*10**2+p*10+q
                            if a == k**5+l**5+i**5+j**5+p**5+q**5:
                                token[a]=[k,l,i,j,p,q]
    return token
# reduce(operator.add,token.keys())
def sum():
    token = result()
    value = 0
    for key in token.keys():
        if key>1:
            print key,token[key]
            value+=key
    return value
print sum()
