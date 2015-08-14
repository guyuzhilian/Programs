# -*- coding:utf-8 -*-
#   author: lidajun
#   date: 2015/7/30
#   time: 10:51

import math

prime_cache = {}

def root_of_quadratic(a, b, c):
    return (-b + math.sqrt(b * b - 4.0 * a * c)) / 2

def is_prime(num):
    if num == 2 or num == 3:
        return True

    if num % 2 == 0:
        return False

    for factor in xrange(3, int(math.sqrt(num)) + 1, 2):
        if num % factor == 0:
            return False

    return True

def main():
    prime_cache[2] = True
    prime_cache[3] = True
    prime_cache[5] = True
    max_len = 0
    for a in xrange(-999, 1000):
        for b in xrange(2, 1000):
            if math.pow(a, 2) - 4 * b >= 0:
                x1 = root_of_quadratic(1, a, b)

                # if the equation has integral root, then the quadratic can be written into (n-x1)(n-x2)
                if x1 == int(x1):
                    continue

            n = 0
            while True:
                value = n * n + a * n + b
                if value >= 2 and is_prime(value):
                    n += 1
                else:
                    break

            if max_len < n:
                max_len = n
                max_a = a
                max_b = b

    print(max_a, max_b, max_len, max_a * max_b)

if __name__ == "__main__":
    main()