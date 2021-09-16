# Created on: 16th September, 2021
# Author: Bharadwaj Yellapragada

# Day 3: Is that an odd multiple of 5?
# Language: Python

def main():
    try:
        number = int(input('Enter a odd multiple of 5:'))
        if number % 2 != 0 and number % 5 == 0:
            print('Well Done!')
        else:
            print('Wrong! Try Again!')
            main()
    except TypeError:
        print('Please enter integers only! Try Again!')
        main()


if __name__ == '__main__':
    main()
