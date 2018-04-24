# coding:utf-8


# 1 ab/bc=a/c
# 2 ab/cb=a/c
# 3 ba/bc=a/c
# 4 ba/cb=a/c
def gcd(a,b):
    if b>a:
        tmp =a
        a= b
        b=tmp
    c=a%b
    if c!=0:
        return gcd(b,c)
    else:
        return b

def fra_method():
    L=[]
    res1= 1
    res2=1
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                i = a*10+b
                j = b*10+c
                m = c*10+b
                n = b*10+a
                if a<c and a!=b and b!=c:
                    if i*c==j*a:
                        print i,j,a,b,c
                        res1*=a
                        res2*=c
                    if i*c==a*m:
                        print i,m,a,b,c
                        res1*=a
                        res2*=c
                    if n*c==a*j:
                        print j,n,a,b,c
                        res1*=a
                        res2*=c
                    if n*c==a*m:
                        print m,n,a,b,c
                        res1*=a
                        res2*=c

    return res2/gcd(res1,res2)

print fra_method()