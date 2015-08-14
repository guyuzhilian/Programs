# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-28 17:05

def main():
    multiple_result = 1
    number_of_factor_ten = 0
    for num in xrange(2, 101):
        while num % 5 == 0:
            num /= 5
            multiple_result /= 2
            number_of_factor_ten += 1

        multiple_result *= num

    # print(multiple_result, number_of_factor_ten)
    print(sum(int(digit) for digit in str(multiple_result)))

if __name__ == "__main__":
    main()