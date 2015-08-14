# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-24 11:42

SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6

# if leap add 1
DAYS_OF_YEAR = 365
DAYS_OF_WEEK = 7

# if leap add 1 to feb
DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

MONTHS_OF_YEAR = 12

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    # 1990 is not a leap year, calculate the weekday of 1 Jan, 1901
    start_weekday = MONDAY + DAYS_OF_YEAR % DAYS_OF_WEEK
    day_of_week = start_weekday
    count_of_sunday = 0
    for year in range(1901, 2001):
        leap = is_leap_year(year)
        for month in range(0, MONTHS_OF_YEAR):
            if day_of_week == SUNDAY:
                print(year, month+1)
                count_of_sunday += 1

            days_of_this_month = DAYS_OF_MONTH[month]
            if leap and month == 1:
                days_of_this_month += 1

            day_of_week += days_of_this_month % 7
            day_of_week %= 7

    return count_of_sunday

if __name__ == "__main__":
    print(main())