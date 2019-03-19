#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-03-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Prints "bottles of beer on the wall" song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    nb = args.num_bottles

    if not nb > 0:
        die("N ({}) must be a positive integer".format(nb))

    max_num = nb + 1

    how_many_phrase = " bottles of beer on the wall,"
    repeat_how_many = " bottles of beer,"
    pass_phrase = "Take one down, pass it around,"
    final_how_many_phrase = " bottles of beer on the wall!\n" 

    one_how_many_phrase = " bottle of beer on the wall,"
    one_repeat_how_many = " bottle of beer,"
    one_pass_phrase = "Take one down, pass it around,"
    one_final_how_many_phrase = " bottle of beer on the wall!\n" 



    nums = reversed(list(range(0, max_num)))

    for bottle in nums:
        if bottle == 0:
            break
        if bottle == 2:
            print("{}{}".format(bottle, how_many_phrase))
            print("{}{}".format(bottle, repeat_how_many))
            print("{}".format(pass_phrase))
            print("{}{}".format(bottle-1, one_final_how_many_phrase))
        if bottle == 1:
            print("{}{}".format(bottle, one_how_many_phrase))
            print("{}{}".format(bottle, one_repeat_how_many))
            print("{}".format(one_pass_phrase))
            print("{}{}".format(bottle-1, final_how_many_phrase))

        if bottle > 2:
            print("{}{}".format(bottle, how_many_phrase))
            print("{}{}".format(bottle, repeat_how_many))
            print("{}".format(pass_phrase))
            print("{}{}".format(bottle-1, final_how_many_phrase)) 



    

# --------------------------------------------------
if __name__ == '__main__':
    main()
