#!/usr/bin/python3
for number1 in range(8):
    for number2 in range(number1 + 1, 10):
        print("{}{}, ".format(number1, number2), end="")

print("89")
