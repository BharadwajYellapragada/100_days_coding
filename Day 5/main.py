# Created on: 16th September, 2021
# Author: Bharadwaj Yellapragada

# Day 5: What is the 6th character in the string
# Language: Python

def main():
    yb_input = input('Enter your input:')
    if len(yb_input)<6:
        print('Entered input does not have a 6th character! Try Again!')
        main()
    else:
        sixth_char = yb_input[5]
        print(sixth_char,'is the sixth character in', yb_input)


if __name__ == '__main__':
    main()
