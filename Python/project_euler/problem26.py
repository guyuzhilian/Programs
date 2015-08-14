# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-29 16:56

def gen_decimal_fraction_part(n):
    assert n < 1000, "n should be less than 1000"
    if n == 1:
        return "1"

    elif n <= 10:
        faction_parts = ["0."]
        index = 1
        dividend = 10
    elif n <= 100:
        faction_parts = ["0.", "0"]
        index = 2
        dividend = 100
    else:
        faction_parts = ["0.", "0", "0"]
        index = 3
        dividend = 1000

    intermediate_remainder = {}
    while dividend != 0 and dividend not in intermediate_remainder:
        intermediate_remainder[dividend] = index

        result = dividend / n

        dividend %= n
        dividend *= 10

        faction_parts.append(str(result))
        index += 1

    if dividend != 0:
        faction_parts.insert(intermediate_remainder[dividend], "(")
        faction_parts.append(")")

    return "".join(faction_parts)

def len_of_recurring_cycle(n):
    assert n < 1000, "n should be less than 1000"
    if n == 1:
        return 0

    elif n <= 10:
        faction_parts = ["0."]
        dividend = 10
    elif n <= 100:
        faction_parts = ["0.0"]
        dividend = 100
    else:
        faction_parts = ["0.00"]
        dividend = 1000

    index = 1
    intermediate_remainder = {}
    while dividend != 0 and dividend not in intermediate_remainder:
        intermediate_remainder[dividend] = index

        result = dividend / n

        dividend %= n
        dividend *= 10

        faction_parts.append(str(result))
        index += 1

    if dividend != 0:
        return index - intermediate_remainder[dividend]

    return 0

def main():
    max_len = 0
    max_num = 0
    for i in xrange(1, 1000):
        if max_len < len_of_recurring_cycle(i):
            max_num = i
            max_len = len_of_recurring_cycle(i)

    print(max_num, max_len, gen_decimal_fraction_part(max_num))

if __name__ == "__main__":
    main()