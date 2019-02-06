#!/usr/bin/env python3
# Write a Python program that will create a square grid from the argument given on the command line. (I suggest but do not require you use new_py.py to start the program.)
# 
# The program will expect one positional argument; if the number of arguments is not exactly one, print a "usage" statement and exit with an error code.
# The test suite will only provide integer values, so you can assume it is safe to use int to convert the input from a string to an integer.
# The number provided must be in the range of 2 to 9 (inclusive). If it is not, print "NUM () must be between 1 and 9" and exit with an error code.
# You will square the given number to create a grid (so think of the number as how many rows and columns).
# Your grids will look like the below.

import sys
import os
import math # for sqrt

def main(): 
	if len(sys.argv) != 2:
		print("Usage: {} NUM".format(os.path.basename(sys.argv[0])))
		sys.exit(1)

	num = int(sys.argv[1])

	if int(num) not in range(2,10):
		print("NUM ({}) must be between 1 and 9".format(num))
		sys.exit(1)


	for x in range(1, num ** 2 + 1):
		print("{:3}".format(x), end = "")
		if x % num == 0:
			print() # empty prints new line

main()
