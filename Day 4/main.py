# Created on: 16th September, 2021
# Author: Bharadwaj Yellapragada

# Day 4: Is the length of the list a even number?
# Language: Python

def main():
    yb_list_odd = ['This','is',1,'list with decimal length',5.0]
    yb_list_even = ['This is another list with integer length',2]
    yb_lists = [yb_list_odd,yb_list_even]

    for yb_list in yb_lists:
        if len(yb_list)%2==0:
            print(yb_list,'has even number of items:',len(yb_list))
        else:
            print(yb_list,'does not have even number of items',len(yb_list))


if __name__ == '__main__':
    main()
