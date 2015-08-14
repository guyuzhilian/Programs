#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author: lidajun
#   date: 2015/7/31
#   time: 10:23

def get_nth_digit(num, n):
    return (num / pow(10, n-1)) % 10

def sum_of_fifth_power(num):
    total = 0
    for n in xrange(1, len(str(num))+1):
        digit = get_nth_digit(num, n)
        total += pow(digit, 5)

    return total

def main():
    total = 0
    for num in xrange(2, 1000000):
        if sum_of_fifth_power(num) == num:
            print(num)
            total += num

    print(total)

if __name__ == "__main__":
    main()