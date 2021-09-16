# Created on: 16th September, 2021
# Author: Bharadwaj Yellapragada

# Day 7: Encrypt your name with alphabetical position of each letter
# Language: Python

def main():
    input_name = input('Enter your name:').lower()
    numbers = []
    for letter in input_name:
        if letter.isalpha():
            numbers.append(str(ord(letter) - 96))
        else:
            numbers.append(letter)
    print("Encrypted name:","".join(numbers))


if __name__ == '__main__':
    main()
