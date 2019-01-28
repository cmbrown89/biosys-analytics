#!/usr/bin/env bash

#Your program will expect to receive an argument in $1 and maybe a second in $2
#If there are no arguments, it should print a "Usage" and exit with an error code
#If the first argument is not a file, it should notify the user and exit with an error code
#If the second argument is missing, use the value "3"
#Print the number of lines requested by the user by iterating over the lines in the file and exiting the loop appropriately

set -u # this makes bash tell me if I mis-wrote or didn't assign variables


# First check number of args is 1
if [[ $# -eq 0 ]]; then
	echo "Usage: head.sh FILE [LINES]"
	exit 4
fi

FILE=$1
LINES=${2:-3} # make optional and default to 3


if [[ ! -f $FILE ]]; then
		echo "$FILE is not a file"
		exit 4
fi

# script: for every iteration, count line being read in, stop if equaled to $LINES
i=0
while read -r LINE; do
	echo $LINE # print next line in each iteration
	i=$((i+1)) # count number of line iteration is on
	if [[ $i -eq $LINES ]]; then # when $LINES == iteration, exit with no errors
		break 
	fi
done < "$FILE"

#awk 'NR<='$LINES' {print}' $FILE

