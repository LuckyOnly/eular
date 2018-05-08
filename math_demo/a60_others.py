# coding:utf-8

from Euler import prime_sieve, is_prime
import itertools as iter

primes =prime_sieve(10000)
set_size = 5


def make_chain(chain):
    if len(chain) == set_size:
        return chain
    for p in primes:
        if p > chain[-1] and all_prime(chain + [p]):
            new_chain = make_chain(chain + [p])
            if new_chain:
                return new_chain
    return False


def all_prime(chain):
    return all(is_prime(int(str(p[0]) + str(p[1]))) for p in iter.permutations(chain, 2))


chain = 0
while not chain:
    chain = make_chain([primes.pop(0)])

print "Project Euler 60 Solution =", sum(map(int, chain)), chain