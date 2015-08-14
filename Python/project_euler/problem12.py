# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-15 15:00

def count_of_factors(num):
    # initial with 2 (1 and itself)
    count = 2
    for i in range(2, num):
        if num % i == 0:
            count += 1

    return count

def main():
    num = 1
    while True:
        print(num)
        if count_of_factors(num) > 500:
            print(num)
            break
        num += 1

if __name__ == "__main__":
    main()