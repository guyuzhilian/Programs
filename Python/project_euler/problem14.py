# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-15 18:36

def len_of_collatz_chain(starting_number):
    # chain length including starting_number
    count = 1
    while starting_number > 1:
        if starting_number % 2 == 0:
            starting_number /= 2
        else:
            starting_number = 3 * starting_number + 1
        count += 1

    return count

def main():
    max_len = 0
    starting_number = 0
    for n in range(2, 1000000):
        length = len_of_collatz_chain(n)
        if max_len < length:
            max_len = length
            starting_number = n

    print(starting_number)

if __name__ == "__main__":
    main()
    # print(len_of_collatz_chain(13))