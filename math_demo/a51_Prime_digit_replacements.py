# coding:utf-8
from prime_distinct import is_prime
L=[]
def construction_primes():
    for  i in xrange(10**5+1,10**6):
        if i%10==3 and is_prime(i):
            L.append(i)
    return L

token={}

def solve_method1():
    L =construction_primes()
    L.sort()
    return L

def solve_method2():
    L =construction_primes()
    L.sort()
    i =0
    j =10
    while i<len(L):
        count = 0
        while  i<len(L) and L[i] / 1000 ==j:
            a = L[i]/10%10
            b = L[i]/100%10
            # c = L[i]/1000%10
            if a==b :#and a==c:
                print L[i]
                count +=1
            i+=1
        if count > 6:
            token[j]=count
        j += 1
    return token
import string
def eight_prime_family(prime,rd):
    c = 0
    for digit in '0123456789':
        n = int(string.replace(prime,rd,digit))
        if n in L:
            c+=1
    return c==8

def solve_method3():
    for prime in L:
        s= str(prime)
        last_digit = s[5:6]
        if (s.count('0')==3 and eight_prime_family(s,'0')) \
            or (s.count('1') == 3 and eight_prime_family(s, '1')) \
            or (s.count('2')==3 and eight_prime_family(s,'2')):
            print 'solution is :'+s




def solve_method():
    L =construction_primes()
    L.sort()
    # count = 0
    i =0
    j =10
    while i<len(L):
        count = 0
        while  i<len(L) and L[i] / 10000 ==j:
            a = L[i]/10%10
            b = L[i]/100%10
            c = L[i]/1000%10
            if a==b and a==c:
                print L[i]
                count +=1
            i+=1
        if count > 0:
            token[j]=count
        j += 1
    return token

L =construction_primes()
L.sort()
solve_method3()
# L =construction_primes()
# L.sort()
# print L[:10]