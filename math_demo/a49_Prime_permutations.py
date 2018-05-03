# coding:utf-8
from prime_distinct import is_prime


def permutation_method(num):
    L = set()
    for i in str(num):
        L.add(i)
    return L


def rule_three_method(S):
    L=set()
    list0 = str(S[0])
    list1 = str(S[1])
    list2 = str(S[2])
    if sorted(list0) == sorted(list1) and sorted(list0) == sorted(list2):
        return True
    return False
    # for i in str(S[0]):
    #     L.add(i)
    # for j in S[1:]:
    #     for m in str(j):
    #         if m not in L:
    #             return False
    # return True



def rule_second_method():
    for num in L:
        i=3330
        if num+i>10000:
            break
        if match_size1(i, num):
            return num,i
    return 0


token={}
def match_size(i, num):
    size = 3
    count = 1
    token[num]=True
    S=[num]
    while count < size and  num + i * count<10**4:
        s = num + i * count
        if s in token:
            if not token[s]:
                return False
        if not is_prime(s):
            token[s]=False
            return False
        count += 1
        token[s]=True
        S.append(s)
    print token
    if rule_three_method(S) and count == size:
        print S
        return True
    return False

def match_size1(i,num):
    size = 3
    count = 1
    S=[num]
    while count < size:
        s = num + i * count
        if s not in L:
            return False
        count += 1
        S.append(s)
    if rule_three_method(S) and count == size:
        print S
        return True
    return False

L=[]
def prime_set():
    for i in range(1489,10000):
        if is_prime(i):
            L.append(i)
prime_set()
# print match_size(3330,1487)
print rule_second_method()
# print rule_three_method([1009, 5059, 9109])
# s='zdcf'
# b="cdfz"
# print sorted(s)==sorted(b)