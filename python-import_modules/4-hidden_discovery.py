#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name_files = dir(hidden_4)
    for index in name_files:
        if index[0] != '_':
            print("{}".format(index))
