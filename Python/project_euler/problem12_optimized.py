# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-15 15:23

def main():
    primes = [2, 3]
    n = 2
    while True:
        num = n * (n + 1) / 2
        num_copy = num
        factors = {}
        for prime in primes:
            while num % prime == 0:
                if prime in factors:
                    factors[prime] += 1
                else:
                    factors[prime] = 1
                num /= prime

            # at this point, num is a prime, append to primes
        if num > 1:
            primes.append(num)

        count_of_factors = 1
        for factor, times in factors.iteritems():
            # 0 - times
            count_of_factors *= times + 1

        if count_of_factors > 500:
            print(num_copy)
            break

        n += 1

if __name__ == "__main__":
    main()