#!/usr/bin/env bash

set -u

# If there are no arguments, print out all the basenames of the files 
# in sorted order

RELPATH="../../data/gapminder/"

# This works

if [[ $# -eq 0 ]]; then
    cd $RELPATH 
    ls | sort
    exit
fi

# If there is an argument, treat it like a regular expression and 
# find files where the basename matches at the beginning of the string
# in a case-insensitive manner and print them in sorted order

REGEX=$1

if [[ $# -eq 1 ]]; then
	cd $RELPATH
	LIST=$(ls | sort)
	find -type f -iname "$REGEX*" | basename | sort 
fi

