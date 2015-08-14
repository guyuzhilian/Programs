# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-29 14:07

factorial_cache = [1, 1]

def init_factorial():
    for i in range(2, 11):
        factorial_cache.append(i * factorial_cache[-1])

def get_nth_permutation(nth):
    # decrease 1, adjust to zero-based
    nth -= 1
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    while len(result) < 10:
        digit_index = nth / factorial_cache[10 - 1 - len(result)]
        nth -= digit_index * factorial_cache[10 - 1 - len(result)]
        result.append(digits[digit_index])
        digits.remove(digits[digit_index])

    return result

def main():
    init_factorial()
    result = get_nth_permutation(1000000)
    print "".join([str(num) for num in result])


if __name__ == "__main__":
    main()