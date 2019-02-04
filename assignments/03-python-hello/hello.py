#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:03:42 2019

@author: clairessabrown
"""
import os
import sys

def main():
    names = sys.argv[1:] # First argument, like in bash is program name
    # Show usage statement if no names provided
    if len(names) == 0:
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
        
    # If len(names) == 1
    if len(names) == 1:
        print("Hello to the 1 of you: " + names[0] + "!")
        
    # If len(names) == 2
    if len(names) == 2:
        print("Hello to the {} of you: {}!".format(len(names), " and ".join(names)))
        
    # If len(names) > 2
    if len(names) > 2:
        names[-1] = "and " + names[-1]
        print("Hello to the {} of you: {}!".format(len(names), ", ".join(names)))

main() # call function when script executed

