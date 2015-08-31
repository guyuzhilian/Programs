#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lidajun
# date: 2015-08-30 20:06

import math
import itertools

circular_primes = {}

def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in xrange(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

def is_circular_prime(num):
    # 1-digit is prime, then it is circular prime
    str_num = str(num)
    if len(str_num) == 1:
        if is_prime(num):
            circular_primes[num] = True
            return True
        else:
            return False

    for i in range(len(str_num)):
        new_num = int(str_num[i:] + str_num[:i])

        if not is_prime(new_num):
            return False

    circular_primes[num] = True
    return True

def main():
    for num in xrange(2, 1000000+1):
        if is_circular_prime(num):
            print(num)

    print(len(circular_primes))
    print(circular_primes)

if __name__ == "__main__":
    main()