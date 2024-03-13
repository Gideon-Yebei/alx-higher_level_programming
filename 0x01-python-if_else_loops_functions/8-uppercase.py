#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:  # ASCII values for lowercase letters
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
