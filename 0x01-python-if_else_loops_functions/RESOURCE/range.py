#!/usr/bin/python3

for i in range(5):
		print(i)

# specify start and end
print(list(range(5,10)))

# specify start, end and step
print(list(range(0, 10, 3)))

# using negatives
print(list(range(-10, -100, -30)))

"""
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):
"""

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
		print(i, a[i])

"""
to iterate over the indices of a sequence, you can combine range() and len() as follows:

NB: in most such cases, however, it is convenient to use the enumerate() function.
"""

print(sum(range(4))) # 0+1+2+3 = 6
"""
The sum() function returns the sum of a sequence of numbers (not a list, but a sequence). The sequence may be any kind of sequence, but it must be a sequence of numbers. The math module has a function of the same name, but it accepts any iterable.
"""
