"""
Solution for https://projecteuler.net/problem=25
Prints the index of the first term in the Fibonacci sequence to contain 1000 digits
"""
from fibonacci import fibonacci, NumberLengthChecker
length = 1000
length_checker = NumberLengthChecker(length)
n = 1
sequence = fibonacci()
while (not length_checker.is_long_enough(next(sequence))):
    n += 1

print("First {}-digit term found at {}".format(length, n))