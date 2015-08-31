#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lidajun
# date: 2015-08-31 13:59

def is_palindromic(num, base = 10):
    if base == 10:
        str_num = str(num)
    else:
        str_num = bin(num)[2:]
    if str_num == str_num[::-1]:
        print(num, base, str_num)
        return True

    return False

def main():
    total = 0
    for num in xrange(1, 1000000):
        if is_palindromic(num, 10) and is_palindromic(num, 2):
            total += num

    print(total)

if __name__ == "__main__":
    main()