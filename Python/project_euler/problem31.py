#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author: lidajun
#   date: 2015/7/31
#   time: 15:56

def main():
    count = 0
    for a in xrange(0, 201):
        for b in xrange(0, 101):
            for c in xrange(0, 41):
                for d in xrange(0, 21):
                    for e in xrange(0, 11):
                        for f in xrange(0, 5):
                            for g in xrange(0, 3):
                                for h in xrange(0, 1):
                                    if a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h == 200:
                                        count += 1

    print(count)

if __name__ == "__main__":
    main()