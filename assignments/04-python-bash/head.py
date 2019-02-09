#! /usr/bin/env python3

"""
It should expect one or two arguments; if there are no arguments, print a "Usage" statement

The first argument is required and much be a regular file; if it is not, print " is not a file" and exit with an error code

The second argument is optional. If given, it must be a positive number (non-zero); if it is not, then print "lines () must be a positive number". If no argument is provided, use a default value of 3. You can expect that the test will only give you a value that can be safely converted to a number using the int function.

If given good input, it should act like the normal head utility and print the expected number of lines from the file
"""

import sys
import os

def main():
	if len(sys.argv[1:]) == 0:
		print("Usage: head.py FILE [NUM_LINES]")
		sys.exit(1)

	args = sys.argv[1:]

	if os.path.isfile(args[0]) != True:
		print("{} is not a file".format(args[0]))
		sys.exit(1)

	file = args[0]

	i = 0


	if len(args[1:]) == 0:
		with open(file) as f:
			for line in f:
				i+=1
				print("{}".format(line), end = "")
				if i == 3: 
					break

	if len(args[1:]) == 1 and int(args[1]) <= 0:
			print("lines ({}) must be a positive number".format(args[1]), end = "")
			sys.exit(1)
	
	if len(args[1:]) == 1 and int(args[1]) > 0:
		with open(file) as f:
			for line in f:
				i+=1
				print("{}".format(line), end = "")
				if i == int(args[1]): 
					break
		

main()
