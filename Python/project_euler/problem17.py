# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-14 16:29

import unittest

NUMBER_TO_WORD = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

TEN_TO_WORD = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

UNIT_TO_WORD = {
    100: "hundred",
    1000: "thousand"
}

def convert_number_to_words_below_100(number):
    if number == 0:
        return ""

    if number in NUMBER_TO_WORD:
        return NUMBER_TO_WORD[number]

    if number < 100:
        ten = number / 10
        one = number % 10

        if one == 0:
            return TEN_TO_WORD[ten]
        else:
            return "%s %s" % (TEN_TO_WORD[ten], NUMBER_TO_WORD[one])

# now support number less than 1000
def convert_number_to_words(number):
    if number < 100:
        return convert_number_to_words_below_100(number)

    elif number < 1000:
        hundred = number / 100
        number_removed_hundred = number % 100

        if number_removed_hundred > 0:
            return "%s hundred and %s" % (NUMBER_TO_WORD[hundred], convert_number_to_words_below_100(number_removed_hundred))
        else:
            return NUMBER_TO_WORD[hundred] + " hundred"
    elif number == 1000:
        return "one thousand"
    else:
        raise ValueError("number is greater than 1000")

def main(lower, upper):
    length = 0
    for i in xrange(lower, upper):
        number_words = convert_number_to_words(i)
        number_words_removing_spaces = number_words.replace(" ", "")
        length += len(number_words_removing_spaces)
        # print("%s %s %d" % (number_words, number_words_removing_spaces, len(number_words_removing_spaces)))
        print(i, len(number_words_removing_spaces))
    return length

class TestConvertNumberToWords(unittest.TestCase):

    # test zero
    def test_zero(self):
        self.assertEqual(convert_number_to_words_below_100(0), "")

    def test_342(self):
        self.assertEqual(convert_number_to_words(342), "three hundred and forty two")

    def test_342_length(self):
        self.assertEqual(len(convert_number_to_words(342).replace(" ", "")), 23)

    def test_115(self):
        self.assertEqual(convert_number_to_words(115), "one hundred and fifteen")

    def test_115_length(self):
        self.assertEqual(len(convert_number_to_words(115).replace(" ", "")), 20)

    def test_1_to_5(self):
        self.assertEqual(main(1, 5 + 1), 19)

    def test_500(self):
        self.assertEqual(convert_number_to_words(500), "five hundred")

if __name__ == "__main__":
    print(main(1, 1000 + 1))
    # unittest.main()