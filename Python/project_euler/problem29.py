#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author: lidajun
#   date: 2015/7/31
#   time: 10:00

primes = [2, 3, 5]
num_factors = {}
def decompose_into_primes(a, b):
    factors = {}
    a_copy = a
    for prime in primes:
        factors[prime] = 0
        while a % prime == 0:
            a /= prime
            factors[prime] += b

    if a != 1:
        primes.append(a)
        factors[a] = b

    num_factors[(a_copy, b)] = factors

def main():
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            decompose_into_primes(a, b)

    unique_set = set()
    for ab, factors in num_factors.iteritems():
        nums = []
        for prime in primes:
            nums.append(factors.get(prime, 0))
        unique_set.add(tuple(nums))

    print(len(unique_set), len(num_factors))


if __name__ == "__main__":
    main()