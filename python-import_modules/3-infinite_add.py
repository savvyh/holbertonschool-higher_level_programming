#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total_args = len(argv) - 1
    result = 0

    for index in range(1, total_args + 1):
        result += int(argv[index])
    print(result)
