#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-03-10
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
import csv


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Parsing BLAST output files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'blast', metavar='FILE', help='BLAST')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

    
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
    blast = args.blast 
    anno = args.annotations  # centroids
    outfile = args.outfile # print stdout to this file

    # Check that input files are files
    for file in [blast, anno]:
        if not os.path.isfile(file):
            die("\"{}\" is not a file".format(file))

    
    # Build another dictionary where seqID is key and last 2 elements are values 
    anno_dict = {}

    with open(anno) as f:
        reader = csv.DictReader(f)
        for row in reader:
            anno_dict[row['centroid']] = row

    #die(dict(anno_dict))

    # Searching anno_dict for seqID, keep in mind it may not be there
<<<<<<< HEAD
    # Don't put blast in dictionary 

   open(outfile, "wb") 
   #write header here)
=======
>>>>>>> 4553067f5eac63d7cfa3c33e0d94386ee41878e6

    with open(blast) as f:
        fieldnames = "qseqid,seq_id,pident,length,mismatch,gapopen,qstart,qend,sstart,send,evalue,bitscore".split(",")
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter="\t")
        for row in reader:
            seqID = row["seq_id"]           
            if seqID in anno_dict:
                genus = anno_dict.get(seqID).get("genus") or "NA"
                species = anno_dict.get(seqID).get("species") or "NA"
<<<<<<< HEAD
                #print(row["seq_id"], row["pident"], genus, species, file=sys.stdout)
                blah = row["seq_id"], row["pident"], genus, species
                
                with 
                    writer = csv.DictWriter(w, delimiter="\t", fieldnames=fieldnames)
                    writer.writeheader()

            else:
                print("Cannot find seq \"{}\" in lookup".format(seqID), file=sys.stderr)

    # close file here

=======
                print(row["seq_id"], row["pident"], genus, species, file=sys.stdout)
            else:
                print("Cannot find seq \"{}\" in lookup".format(seqID), file=sys.stderr)

>>>>>>> 4553067f5eac63d7cfa3c33e0d94386ee41878e6

    # To do: Print found output to standard out, non-found to standard error
    # To do: Get header in output file
    #if len(outfile) != 0:
    #    with open(outfile, "w").write()



<<<<<<< HEAD
# with open(outfile,'wb') as fou:
#     dw = csv.DictWriter(fou, delimiter='\t', fieldnames=ordered_fieldnames)
#     dw.writeheader()

=======
>>>>>>> 4553067f5eac63d7cfa3c33e0d94386ee41878e6

   
# --------------------------------------------------
if __name__ == '__main__':
    main()
<<<<<<< HEAD
=======

>>>>>>> 4553067f5eac63d7cfa3c33e0d94386ee41878e6
