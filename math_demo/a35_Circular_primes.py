# coding:utf-8
import math
def is_prime(num):
    size = int(math.sqrt(num))
    i=2
    while i<= size:
        if num % i == 0:
            return False
        i+=1
    return True

from itertools import combinations,permutations
def check(num):
    mul =1
    while mul<num:
        mul*=10
    mul/=10
    tmp = num
    while True:
        if tmp%10==0:
            return False
        tmp = tmp/10+tmp%10*mul
        if not is_prime(tmp):
            return False
        if tmp==num:
            break
    return True

def permu_method(num):
    L=[]
    T=[]
    s = str(num)
    for i in s:
        L.append(int(i))
    S = list(permutations(L,len(L)))
    i = 0
    while i <len(S):
        j= 0
        l=len(L)
        tmp = 0
        while j < l:
            tmp +=S[i][j]*10**(l-1-j)
            j+=1
        T.append(tmp)
        i+=1
    for t in T:
        if not is_prime(t):
            return False
    return True


def circular_method(num):
    count = 0
    for i in range(2,num+1):
        if is_prime(i):
            if check(i):
                print i
                count +=1

    return count
print circular_method(1000000)



# print check(197)
