#!/usr/bin/env python3

import os
import argparse
import sys
import csv 
from collections import defaultdict


# Get command line arguments
def args():
	parser = argparse.ArgumentParser(
		description = "Print first lines of files in folder")

	# Directory(ies)
	# fold
	parser.add_argument(
		"positional",
		metavar = "DIR",
		nargs = "+")

	# width
	parser.add_argument(
		"-w",
		"--width",
		metavar = "int",
		type = int,
		default = 50)

	return parser.parse_args()
args()


# Kill
def kill():
	if len(sys.argv) == 1:
		print("{}: error: the following arguments are required: DIR".format(os.path.basename(sys.argv[0])))
		sys.exit(1)

	fold = args().positional

	# Eventually print this to standard error
	for d in fold: 
		if not os.path.isdir(d) == True:
			print("\"{}\" is not a directory".format(d))

kill()

# Main
def main():
	fold = args().positional
	width = args().width


	i = 0
	for folder in fold:
		for file in os.listdir(folder):
			with open(os.path.join(folder,file)) as f:
				for line in f:
					i+=1
					print("{}:{}".format(f, line), end = "")
					if i == 1:
						break



# test
#with open()


#if len(args[1:]) == 1 and int(args[1]) > 0:
#	with open(file) as f:
#		for line in f:
#			i+=1
#			print("{}".format(line), end = "")
#			if i == int(args[1]): 
#				break
		
		
		
		
		#	reader = csv.DictReader(f, delimiter = "\t")
		#	for line in reader:
		#		print(line)



#	with open(file) as f:
#		for line in f:
#			i += 1
#			print(" {:3}: {}".format(i, line), end = "")




main()

