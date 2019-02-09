#! /usr/bin/env python3

"""
It should expect exactly one argument which is a regular file; if either condition fails, print a "Usage" statement

It should print each line of the file argument preceeded by the line number which is right-justified in spaces and a colon. You may use format strings to make it look exactly like the output below, but the test is just checking for a leading space, some number(s), a colon, and whatever else.
"""

import sys # get arguments
import os # access file system

def main():
	if len(sys.argv[1:]) != 1:
		print("Usage: cat_n.py FILE")
		sys.exit(1)

	file = sys.argv[1]

	if os.path.isfile(file) == False:
		print("{} is not a file".format(file), end = "")
		sys.exit(1)

	i = 0

	with open(file) as f:
		for line in f:
			i += 1
			print(" {:3}: {}".format(i, line), end = "")

main()
