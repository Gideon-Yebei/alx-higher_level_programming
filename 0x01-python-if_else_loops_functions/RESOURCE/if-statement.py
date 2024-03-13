#!/usr/bin/python3

x=int(input("Please enter an integer: "))
if x<0:
		x=0
		print('Negative changed to zero')
elif x==0:
		print('Zero')
elif x==1:
		print('Single')
else:
		print('More')

"""
There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
"""
