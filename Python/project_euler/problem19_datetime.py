# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-28 16:56

import datetime

def main():
    count_of_sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                count_of_sundays += 1

    print(count_of_sundays)

if __name__ == "__main__":
    main()