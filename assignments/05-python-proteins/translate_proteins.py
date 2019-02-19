#!/usr/bin/env python3

"""
Write a Python program called "translate_proteins.py" that translates a given DNA/RNA sequence to amino acids using a provided codon table. The output will be written to a file either provided by the user or a default of "out.txt".
"""

import argparse
import sys # for exiting with error
import os # for checking for file existence

# Get command-line arguments
def get_args():
	parser = argparse.ArgumentParser(
		description = "Translate DNA/RNA sequences to protein codons.")

	# test
	parser.add_argument(
		"positional",
		metavar = "STR",
		help = "DNA/RNA sequence")

	# codon
	parser.add_argument(
		"-c", 
		"--codons",
		metavar = "FILE",
		type = str,
		help = "A file with codon translations (default: None)",
		required = True)

	# optional output file
	parser.add_argument(
		"-o",
		"--outfile",
		metavar = "FILE",
		help = "Output filename (default: None)",
		default = "out.txt")

	return parser.parse_args() # for downstream functions

get_args()


# Kill if --codons is not a file
def kill():
	args = get_args()
	c = args.codons

	if os.path.isfile(c) == False:
		print("--codons \"{}\" is not a file".format(c))
		sys.exit(1)

kill()

# Make sure to make this all case-insensitive but converting to uppercase
def main():
	args = get_args()
	c = args.codons # provided codon file (can be dna or rna)
	nuc_acids = args.positional.upper() # given codon(s) STR
	out = args.outfile

	# Fill empty dictionary with codon file and format it into a dictionary with codons as keys and amino acids as values
	codon_tab = {}

	# Get codons and proteins and fill codon dictionary
	with open(c) as file:
		for line in file:
			codon, protein = line.split()
			codon_tab[codon] = protein # assigning value to keys to build codon-protein dictionary

	k = 3 # slides in window of 3, same length of codon
	n = len(nuc_acids) - k + 1
	
	out_fh = open(out, "wt")

	for i in range(0,n,k):
		codon = nuc_acids[i:i+k]
		out_fh.write(codon_tab.get(codon, "-"))
	out_fh.write("\n")
	out_fh.close()
	print("Output written to \"{}\"".format(out))


main()


