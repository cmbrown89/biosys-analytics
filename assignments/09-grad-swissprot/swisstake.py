#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-03-19
Purpose: Filter swissprot file by taxa and look for certain keywords 
"""

import argparse
import sys
from Bio import SeqIO
import re
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Parse Swissprot file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE', help='A Swissprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip records by given taxa',
        metavar='STR',
        type=str,
        nargs="+",
        default=None)
   
    parser.add_argument(
        '-k',
        '--keyword',
        help='Keyword to search for',
        metavar='STR',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='output file',
        metavar='FILE',
        type=str,
        default='out.fa')

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
    swiss = args.file
    keyword = args.keyword
    skip = args.skip
    out = args.outfile


    if not os.path.isfile(swiss):
        die("\"{}\" is not a file".format(swiss)) 

    if skip is not None:
        set_skip = set([e.upper() for e in skip])


    if len(keyword) > 1:
        set_keyword = set([keyword.upper()])

    num_skipped = 0
    num_taken = 0


    print("Processing \"swiss.txt\"")

    with open(out, "w") as outfh:
        for record in SeqIO.parse(swiss, "swiss"):
            annotations = record.annotations # call r.a dict annotations
            if skip and "taxonomy"  in annotations: # if the words to skip AND the category "taxonomy" is in the record dictionary, check for certain conditions below...
                # iterate through each record in the record dict (annotations) and make taxonomy list into a set
                taxa = set(map(str.upper, annotations["taxonomy"])) 
                if set_skip.intersection(taxa): # if the skip words intesect with any of the taxonomy...
                    num_skipped +=1 # count this as part of records skipped
                    continue # and then move on and continue the loop
            if "keywords" in annotations: # check if category keywords in record dict,...
                kw = set(map(str.upper, annotations["keywords"])) # if it is make keywords in record dict into a set
                if kw.intersection(set_keyword): # if keywords from user intersect with keywords from record dict
                    num_taken += 1 # count as taken
                    SeqIO.write(record, outfh, "fasta") # and write the record that matches this keyword to the ooutfile
                else:                      
                    num_skipped +=1 # else, count as skipped

    print("Done, skipped {} and took {}. See output in \"{}\".".format(num_skipped, num_taken, out))


# --------------------------------------------------
if __name__ == '__main__':
    main()


