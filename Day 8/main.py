# Created on: 17th September, 2021
# Author: Bharadwaj Yellapragada

# Day 8: Separate alphanumerical string into list of alphabets and numbers
# Language: Python

def main():
    input_name = input('Enter input:')
    alphabets = []
    numbers = []
    input_error = False
    for letter in input_name:
        if letter.isalpha():
            alphabets.append(letter)
        elif letter.isdigit():
            numbers.append(letter)
        else:
            print('Enter only alphanumeric characters!')
            input_error = True
            break
    if input_error:
        main()
    else:
        print("alphabets:",alphabets)
        print("numbers:", numbers)


if __name__ == '__main__':
    main()
