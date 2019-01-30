#!/usr/bin/env bash

set -u # this makes bash tell me if I mis-wrote or didn't assign variables


# First make sure the number of args make sense
if [[ $# -eq 0 ]]; then
	echo "Usage: hello.sh GREETING [NAME]"
	exit 4
fi


if [[ $# -gt 2 ]]; then
	echo "Usage: hello.sh GREETING [NAME]"
	exit 4
fi

GREETING=$1
NAME=${2:-"Human"}

printf "$GREETING, ""$NAME!\n"


