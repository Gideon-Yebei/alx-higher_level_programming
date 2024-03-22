#!/usr/bin/python3

"""
This script demonstrates the use of the 'break' and 'else' statements in Python loops.
It iterates over a range of numbers and checks if each number is prime or not.
If a number is not prime, it prints the factors of the number.
If a number is prime, it prints that the number is a prime number.
"""
print("############ using break ############")
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')

# continue
# The continue statement, also borrowed from C, continues with the next iteration of the loop:
		print("############ using continue ############")
		for num in range(2, 10):
				if num % 2 == 0:
						print("Found an even number", num)
						continue
				print("Found an odd number", num)
# The pass statement
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:
		print("############ using pass ############")
		while True:
				pass
# This is commonly used for creating minimal classes:
		print("############ using pass in minimal classes ############")
		class MyEmptyClass:
				pass
# Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:
		print("############ using pass as a place-holder ############")
		def initlog(*args):
				pass


