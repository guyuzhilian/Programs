# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-29 15:43

def main():
    fib1 = 1
    fib2 = 1

    index = 2
    while fib2 < pow(10, 999):
        fib1, fab2 = fib2, fib1 + fib2
        index += 1

    print(fib2)
    print(index)

if __name__ == "__main__":
    main()