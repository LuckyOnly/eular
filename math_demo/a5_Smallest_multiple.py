# coding:utf-8


def gcd(n1,n2):
    """greatest common divisor function """
    return gcd(n2, n1 % n2) if n2 > 0 else n1

def lcm(n1,n2):
    """lowest common multiple function"""
    return n1 * n2 // gcd(n1, n2)


def result(num):

    L=[]
    for i in range(1,num+1):
        L.append(i)
    return lcm_name(L)


def lcm_name(L):
    sum = []
    i = 0
    j = len(L) - 1
    if j==0:
        return L
    while i <= j:
        sum.append(lcm(L[i], L[j]))
        i += 1
        j -= 1
    return lcm_name(sum)


print lcm_name(result(20))