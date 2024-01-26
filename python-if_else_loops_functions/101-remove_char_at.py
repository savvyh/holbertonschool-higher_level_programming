#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = str[0:n] + str[n + 1:]
    if n < 0:
        return str
    return new_string
