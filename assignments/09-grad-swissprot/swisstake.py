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


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Parse Swissprot file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='str', help='A Swissprot file')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Keyword to search for',
        metavar='keyword to match',
        type=str,
        require=True)

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip records by given taxa',
        metavar='str',
        type=str,
        nargs="+")

    parser.add_argument(
        '-o',
        '--outfile',
        help='output file',
        metavar='str',
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


    # Read in records to dictionary (annotations)
    # Search for keyword

    print("Processing \"swiss.txt\"")



    """
    Goal: search all keywords for keywords, skip certain keywords or taxa
    - make user input sets for easy comparisons
    - skip to decrease computation time
    - 

    """

    set_skip = set([e.upper() for e in skip])
    set_keyword = set([keyword.upper()])

    num_skipped = 0
    num_taken = 0
    

    with open(outfile, "w") as outfh:
    for record in SeqIO.parse(swiss, "swiss"):
        annotations = record.annotations
        if set_skip and "taxonomy"  in annotations:
            taxa = set(map(str.lower, annotations["taxonomy"]))
            if set_skip.intersection(taxa):
                num_skipped +=1
                continue
            if "keywords" in annotations:
                kw = set(map(str.lower, annotations["keywords"]))

                if k in kw: # or make a set operation since both are
                    num_taken+=1
                    SeqIO.write(record, outfh, "fasta")
                else:
                    num_skipped+= 1

    print("Done, skipped {} and took {}. See output in \"{}\"".format(num_skipped, num_taken, outfh))
    





def blah():

    """main"""
    args = get_args()
    file = args.file
    
    for i, record in enumerate(SeqIO.parse(file, "swiss"), start=1):
        # printing number and record id
        print('{:3}: {}'.format(i, record.id))
        annotations = record.annotations
        
        # below record id...
        for annot_type in ['accessions', 'keywords', 'taxonomy']:
            if annot_type in annotations: # search annotations dict for above list
                print('\tANNOT {}:'.format(annot_type)) 
                val = annotations[annot_type] # search for elements of above list in annotations
                if type(val) is list:
                    for v in val:
                        print('\t\t{}'.format(v))
                else:
                    print('\t\t{}'.format(val))


# --------------------------------------------------
if __name__ == '__main__':
    main()


swiss = "swiss.txt"
for record in SeqIO.parse(swiss, "swiss"):
    annotations = record.annotations
    print(annotations)