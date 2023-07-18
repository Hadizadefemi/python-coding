#!/usr/bin/python3
for digit1 in range(9):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print(89)
        else:
            print(str(digit1 % 10) + str(digit2 % 10), end=", ")
