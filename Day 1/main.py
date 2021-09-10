# Created on: 10th September, 2021
# Author: Bharadwaj Yellapragada

# Day 1: How many days went since I born?
# Language: Python

import datetime

def main():
    date = input("Enter your birthday in dd-mm-yyy format: ")
    date_obj = datetime.datetime.strptime(date, '%d-%m-%Y').date()
    today = datetime.date.today()
    print("Congratulations!, It's been",(today-date_obj).days,"days since you born.")

if __name__ == '__main__':
    main()