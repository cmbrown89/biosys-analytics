#!/usr/bin/env bash

# Make program that prints file and line numbers of each line
# This should receive 1 argument
# This should have a usage statement if running program with no arguments
# This should check if the user inputted a file


set -u

# First check # of args is 1
if [[ ! $# -eq 1 ]]; then
	echo "Usage: cat-n.sh FILE"
	exit 1
fi	

FILE=$1

# If input is a file, print text with line numbers
if [[ ! -f $FILE ]]; then 
	echo "$FILE is not a file" 
	exit 1
fi

COUNTER=0

while read -r LINE; do
	COUNTER=$((COUNTER+1));
	echo "$COUNTER $LINE"; done < "$FILE"	



