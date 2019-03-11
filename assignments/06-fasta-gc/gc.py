#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-03-09
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FASTA', help='str', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Percent GC designator',
        metavar='int',
        type=int,
        choices=range(1,101),
        default=50)

    #parser.add_argument(
    #    '-f', '--flag', help='A boolean flag', action='store_true')

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
    """
    What do I need to do:
    >> Sort files by whether their GC content is considered high or low
    >> Make folders to hold high and low GC content files
    >> Move high files to high folder and low to low folder
    """
    args = get_args()
    pct_gc_int = args.pct_gc 
    fasta = args.fasta
    outdir = args.outdir
    
    # Accept 1+ fasta files and check that they're files
    for file in fasta:
        if not os.path.isfile(file):
            warn(file + " is not a file")
        continue   

    # Check that pct_gc_int is logical, between 1 and 100
    if 0 > pct_gc_int > 101:
        print("You picked \"{}\" for GC designator, please choose integer between 1 and 100".format(pct_gc_int))

    # Accept optional output directory & create if doesn't exists
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
        print("Creating {}".format(outdir))

    # First make loop that only prints out lines with sequences in them
    # Created nested dictionary where each file has base counts
    bases = {} 
    gc_per_file = {} # created every file had it's own dictionary?

    for file in fasta:
        with open(file) as f:
            for line in f:
                match = re.search(">", line)
                if match:
                    continue
                for base in line.rstrip():
                    bases[base] = bases.setdefault(base, 0) + 1
        gc_per_file[file] = bases

    #print(gc_per_file)

    # Math: Calculate GC content by adding all bases together
    # Now need to calculate GC content per file and sort files
    
    files_dict = {}

    for file in gc_per_file.items(): # level: dictionary entry
        for base_counts in file.items(): # level: nested 
            print(base.counts.keys())
        #    g_pct = file.get()





        #for key in base_counts:
        #    g_pct = key.get("G")/sum(key.values())
        #    c_pct = key.get("C")/sum(key.values())
        #    #print(key)        
        #files_dict[file] = int(100 * (g_pct + c_pct))
     
    #print(files_dict)


# --------------------------------------------------
if __name__ == '__main__':
    main()


#>>> people
#{1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#>>> people.get(1)
#{'name': 'John', 'age': '27', 'sex': 'Male'}
#>>> people.get(1).get("name")
#'John'
#>>>












