#!/usr/bin/env bash

#set -u

# If there are no arguments, print out all the basenames of the files 
# in sorted order

RELPATH="../../data/gapminder/"
FILES=$(mktemp)

#mv $RELPATHall.txt $RELPATHall.cc.txt

i=0
if [[ $# -eq 0 ]]; then
	find $RELPATH -type f -iname "*" | sort > "$FILES"
 	while read -r LINE; do
		i=$((i+1))
		BASENAME=$(basename $LINE .cc.txt)
 	    printf "    $i $BASENAME\n"
		done < "$FILES"
fi

# If there is an argument, treat it like a regular expression and 
# find files where the basename matches at the beginning of the string
# in a case-insensitive manner and print them in sorted order

# If no files are found, print a message telling the user

REGEX=$1

find $RELPATH -type f -iname "$REGEX*" | sort > $FILES
NUM_FILES=$(wc -l "$FILES" | awk '{print $1}')

if [[ $NUM_FILES -lt 1 ]]; then
	printf "There are no countries starting with \"%s\"\n" $REGEX
fi


if [[ $NUM_FILES -gt 1 ]]; then
	while read -r LINE; do
	i=$((i+1))
	BASENAME=$(basename "$LINE" .cc.txt)
    printf "%4d  %s\n" $i $BASENAME
	done < "$FILES"
fi


# loop to get line numbers from error message in test.py
#i=0
#while read -r LINE; do
#	i=$((i+1))
#	echo "$i $LINE"
#done < test.py




