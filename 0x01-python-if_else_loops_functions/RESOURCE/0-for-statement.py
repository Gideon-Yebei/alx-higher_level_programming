#!/usr/bin/python3

# measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
		print(w, len(w))

"""
The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):
"""
