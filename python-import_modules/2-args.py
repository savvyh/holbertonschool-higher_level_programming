#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    number_args = len(argv) - 1
    if number_args == 0:
        print("{} arguments.".format(number_args))

    elif number_args == 1:
        print("{} argument:" .format(number_args))

    else:
        print("{} arguments :".format(number_args))

    number = 0
    for index in argv:
        if number != 0:
            print("{}: {}".format(number, index))
        number += 1
