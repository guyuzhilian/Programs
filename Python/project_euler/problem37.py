#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lidajun
# date: 2015-08-31 14:09

import math

def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in xrange(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

def is_interesting_prime(num):
    num_copy = num
    digit_total = 0
    while num_copy > 0:
        d = num_copy % 10
        if d % 2 == 0 or d == 5 or d == 1:
            return False

        digit_total += d
        num_copy /= 10

    if digit_total % 3 == 0:
        return False

    str_num = str(num)
    num_copy = num
    for i in range(len(str_num)):
        if not is_prime(num_copy):
            return False
        num_copy /= 10

    num_copy = num
    for i in range(len(str_num), 1, -1):
        if not is_prime(num_copy % pow(10, i-1)):
            return False

    return True

def main():
    total = 0
    count = 0

    num = 13
    while count < 11:
        if is_interesting_prime(num):
            print(num)
            count += 1
            total += num
        num += 2

if __name__ == "__main__":
    main()