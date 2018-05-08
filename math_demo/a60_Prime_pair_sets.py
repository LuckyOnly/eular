# coding:utf-8
from Euler import miller_rabin,is_prime,prime_sieve
# [13, 5197, 5701, 6733, 8389]
primes = prime_sieve(10000)
set_sieve = 5

def make_chains(chain):
    if len(chain)==set_sieve:
        return chain
    for p in primes:
        if p>chain[-1] and all_prime(chain+[p]):
            new_chain = make_chains(chain+[p])
            if new_chain:
                return new_chain
    return False

import itertools as iter
def all_prime(chain):
    return all(is_prime(int(str(p[0])+str(p[1]))) for p in iter.permutations(chain,2))

# def find_five():
#     i = 8389
#     L=[3,7,109,673]
#     while True:
#         if miller_rabin(i):
#             t= 0
#             while t<len(L):
#                 j = L[t]
#                 a = i*10**len(str(j))+j
#                 b = j*10**len(str(i))+i
#                 print i
#                 if is_prime(a) and is_prime(b):
#                     t+=1
#                 else:
#                     break
#             if t==4:
#                 return i
#         i+=1

chain = 0
while not chain:
    chain=make_chains([primes.pop(0)])

print 'Euler 60 is ',chain,sum(map(int,chain))