#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lidajun
# date: 2015-08-30 17:02

factorial_cache = [1, 1]

def init_factorials():
    for i in range(2, 10):
        factorial_cache.append(factorial_cache[i-1] * i)

def get_n_digit(num, n):
    return int(num // pow(10, n-1) % 10)

def is_the_curious_number(num):
    total = 0
    for i in range(1, len(str(num)) + 1):
        total += factorial_cache[get_n_digit(num, i)]

    return total == num

def main():
    init_factorials()
    total = 0
    for num in range(10, factorial_cache[9] * 7):
        if is_the_curious_number(num):
            print(num)
            total += num
    print(total)

if __name__ == "__main__":
    main()