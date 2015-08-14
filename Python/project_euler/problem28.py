#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author: lidajun
#   date: 2015/7/31
#   time: 9:31

def main(length):
    sum = 0
    prev_n = 1
    for n in xrange(1, length+1, 2):
        while True:
            prev_n += n-1
            sum += prev_n
            if prev_n >= n*n:
                break
    print(sum)

if __name__ == "__main__":
    main(1001)