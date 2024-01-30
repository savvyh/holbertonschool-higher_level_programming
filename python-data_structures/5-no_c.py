#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for index in my_string:
        if index == 'C' or index == 'c':
            continue
        else:
            new_string += index
    return new_string
