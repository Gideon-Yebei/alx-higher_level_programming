#!/usr/bin/python3
def uppercase(str):
    # Create a new string to store the uppercase string
    new_str = ""
    # Loop through each character in the string
    for i in range(len(str)):
        # If the character is a lowercase letter, convert it to uppercase
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_str += chr(ord(str[i]) - 32)
        # Otherwise, keep the character as is
        else:
            new_str += str[i]
    print(new_str)
