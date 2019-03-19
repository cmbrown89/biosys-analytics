#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-01-31
Purpose: Greet user-inputted names with proper punctuation
"""

import os # for accessing file system
import sys # for accessing arguments


# --------------------------------------------------
def main():
    names = sys.argv[1:] # First argument, like in bash is program name

    # Show usage statement if no names provided
    if len(names) == 0: 
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    # If 1 name provided...
    if len(names) == 1:
        print('Hello to the 1 of you: ' + names[0] + '!')
    
    # If over one name - amend last name with "and" and exclamation point
    if len(names) > 2:
        names[-1] = " and " + names[-1]
        print("Hello to the {} of you: {}!".format(len(names), "and ".join(names))


    #if len(names) > 2:
    #    names[-1] = " and " + names[-1]
    #    print("Hello to the {} of you: {}!").format(len(names), ", ".join(names))


    #elif len(names)==2:
    #    print("Hello to the 2 of you: {}!".format(" and ".join(names)))
    #elif len(names)==3:
    #    names[-1] = " and " + names[-1]
    #    print("Hello to the 3 of you: {}!".format(num, " , ".join(names)))
# --------------------------------------------------
main()


# or
#lastname=names.pop()
#"Hellow to the {} of uyou: {} {}!".format(3, names, lastname)

# could also do for loop and have last element behave differently
