# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-28 17:16

sum_cache = {}

def sum_of_proper_divisors(num):
    sum = 1
    for divisor in xrange(2, num/2 + 1):
        if num % divisor == 0:
            sum += divisor

    return sum

def main():
    amicables_sum = 0
    for num in xrange(2, 10000):
        if num not in sum_cache:
            divisors_sum = sum_of_proper_divisors(num)
            if divisors_sum < 10000 and divisors_sum != num:
                if divisors_sum in sum_cache:
                    pass
                else:
                    sum_cache[divisors_sum] = sum_of_proper_divisors(divisors_sum)

                if sum_cache[divisors_sum] == num:
                    print(num, divisors_sum)
                    amicables_sum += num + divisors_sum
                    sum_cache[num] = divisors_sum
                    sum_cache[divisors_sum] = num

    print(amicables_sum)


if __name__ == "__main__":
    main()