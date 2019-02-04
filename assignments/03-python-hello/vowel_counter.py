#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:34:30 2019

@author: clairessabrown
"""

import sys
import os

# count the number of vowels in a single string.
def main():
    args = sys.argv[1:] 
    
    if len(args) != 1:
        print("Usage: {} STRING".format(os.path.basename(sys.argv[0])))
        sys.exit(1)
   
    str = args[0]

    #why doesn't str = sys.argv[1:] work?
    
    # aeiou
    count_a, count_e, count_i, count_o, count_u = 0, 0, 0, 0, 0
   
    
    for letter in str:
        if letter == "a" or letter == "A":
            count_a += 1
        
        elif letter == "e" or letter == "E":
            count_e += 1
        
        elif letter == "i" or letter == "I":
            count_i += 1
        
        elif letter == "o" or letter == "O":
            count_o += 1
        
        elif letter == "u" or letter == "U":
            count_u += 1
        
    sum = count_a + count_e + count_i + count_o + count_u
    
    if sum == 1:
        print('There is {} vowel in "{}."'.format(sum, str))
    else:
        print('There are {} vowels in "{}."'.format(sum, str))   
main()

