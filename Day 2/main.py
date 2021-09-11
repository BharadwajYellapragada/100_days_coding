# Created on: 11th September, 2021
# Author: Bharadwaj Yellapragada

# Day 2: Is that a leap year??
# Language: Python

import datetime


def main():
    try:
        year = int(input("Enter Year: "))
        if year <= 0:
            raise ValueError
    except ValueError:
        print("Please enter only a number greater than 0")
        return 0
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        print("woohoo! its a leap year buddy!")
    else:
        print("not a leap year dude!")


if __name__ == '__main__':
    main()
