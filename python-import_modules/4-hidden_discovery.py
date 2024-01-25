#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    total_files = dir(hidden_4)
    for index in total_files:
        if index == '_':
            continue
    print("{}".format(index))
