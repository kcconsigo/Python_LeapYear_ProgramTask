#Create a#method/function that will identify/return
#the end month date with a given month and year.

import calendar
from datetime import datetime


def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = 0
month = 0


while True:
    try:
        year = int(input("Enter a year: "))
        month = int(input("Enter a month: "))
        days = days_in_month(year, month)
        print(days)

        if calendar.isleap(year):
            print(print("It is a leap year"))
        else:
            print("It is not a leap year")

        x = calendar.month(year, month)
        print("\nDisplay the Calendar:", x)
    except ValueError:
        year = int(input("Enter a year: "))
        month = int(input("Enter a month: "))

        continue
    if year == 2020 and month == 2:
        print(f'You entered: {year}')
        print(f'You entered: {month}')
        break
    else:
        print('Example Data')






