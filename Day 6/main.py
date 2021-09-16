# Created on: 16th September, 2021
# Author: Bharadwaj Yellapragada

# Day 6: How many characters are common in both strings?
# Language: Python

def main():
    yb_string_1 = input("Enter first Word/Sentence:")
    yb_string_2 = input("Enter second Word/Sentence:")

    yb_sent_1_lst = yb_string_1.split(' ')
    yb_sent_2_lst = yb_string_2.split(' ')
    yb_string_1 = yb_string_1.replace(" ", "")
    yb_string_2 = yb_string_2.replace(" ", "")

    common_chars = set(yb_string_1).intersection(set(yb_string_2))
    print("There are", len(common_chars), "charecters common in both inputs:", common_chars)

    if len(yb_sent_2_lst) >1 or len(yb_sent_1_lst)>1:
        common_words = set(yb_sent_1_lst).intersection(yb_sent_2_lst)
        print("There are",len(common_words),"words common in both inputs:",common_words)
    else:
        print("There are no words common in both inputs")



if __name__ == '__main__':
    main()
