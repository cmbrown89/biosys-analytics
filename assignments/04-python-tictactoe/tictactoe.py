#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-02-11
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """make function that gets command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    #parser.add_argument(
    #    'positional', 
    #    metavar='str', 
    #    help='A positional argument')

    # State
    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    # Player
    parser.add_argument(
        '-p',
        '--player',
        help = 'Player',
        metavar = 'str',
        type = str,
        default = ' ')

    # Cell
    parser.add_argument(
        '-c',
        '--cell',
        help = 'Cell to apply -p',
        metavar = 'str',
        type = int,
        default = ' ')


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
    """Tictactoe game"""
    args = get_args() # call function holding arguments
    str_arg = args.arg
    int_arg = args.int
    flag_arg = args.flag
    pos_arg = args.positional
    print('str_arg = "{}"'.format(str_arg))
    print('int_arg = "{}"'.format(int_arg))
    print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))


    

# --------------------------------------------------
if __name__ == '__main__':
    main()
