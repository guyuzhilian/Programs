# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-28 20:09

PERFECT = 1
DEFICIENT = 2
ABUNDANT = 3

num_type_cache = {}

def get_divisor_sum(num):
    sum = 0
    for divisor in xrange(1, num/2+1):
        if num % divisor == 0:
           sum += divisor

    return sum

def get_num_type(num):
    if num in num_type_cache:
        return num_type_cache[num]

    else:
        divisor_sum = get_divisor_sum(num)
        if divisor_sum == num:
            num_type = PERFECT
        elif divisor_sum < num:
            num_type = DEFICIENT
        else:
            num_type = ABUNDANT

        num_type_cache[num] = num_type

        return num_type

def sum_of_two_abundant_number(num):
    for part in xrange(2, num/2+1):
        if get_num_type(part) == ABUNDANT and get_num_type(num - part) == ABUNDANT:
            return True
    return False

def main():
    sum = 0
    for num in xrange(1, 28124):
        if not sum_of_two_abundant_number(num):
            sum += num

    print(sum)

if __name__ == "__main__":
    main()