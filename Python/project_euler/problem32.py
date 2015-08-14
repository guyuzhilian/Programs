#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author: lidajun
#   date: 2015/7/31
#   time: 17:44

def is_pandigital(product_str):
    if len(product_str) != 9:
        return False

    digit_used = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for char in product_str:
        digit = ord(char) - ord('0')
        if digit_used[digit] == 0:
            digit_used[digit] += 1
        else:
            return False

    return True

def main():
    product_map = {}
    for multiplicand in xrange(11, 99):
        for multiplier in xrange(111, 999):
            product = multiplicand * multiplier
            if is_pandigital("%d%d%d" % (multiplicand, multiplier, product)):
                product_map[product] = True

    for multiplicand in xrange(2, 10):
        for multiplier in xrange(1111, 9999):
            product = multiplicand * multiplier
            if is_pandigital("%d%d%d" % (multiplicand, multiplier, product)):
                product_map[product] = True

    total = 0
    for product in product_map:
        total += product

    print(total)

if __name__ == "__main__":
    main()