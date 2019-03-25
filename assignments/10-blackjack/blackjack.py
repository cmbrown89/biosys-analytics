#!/usr/bin/env python3
"""
Author : clairessabrown
Date   : 2019-03-23
Purpose: Play Blackjack
"""

import argparse
import sys
import os
import random
import itertools as it


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Play Blackjack',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='A named string argument',
        metavar='INT',
        type=int,
        default=None)

    parser.add_argument(
        '-p', '--player_hits', help='BOOLEAN', action='store_true')

    parser.add_argument(
        '-d', '--dealer_hits', help='BOOLEAN', action='store_true')

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
def participant_score(hand):
    # Return participant score from cards
    for card_score in hand:
        if type(card_score) is list:
            for num in card_score:
                score = card_score[1]
        if type(card_score) is int:
            score = card_score
    return score

# --------------------------------------------------
def suite_printer(hand):
    # Return suite from cards
    for card_score in hand:
        if type(card_score) is list:
            for num in card_score:
                score = card_score[1]
        if type(card_score) is int:
            score = card_score
    return score



# --------------------------------------------------
def main():
    # Blackjack
    args = get_args()
    seed = args.seed

    ################ Still need to add in -p and -d functionality

    # seed: sets random seed (opt.) for test suite
    if type(seed) is not None:
        random.seed(seed)
    
    suites = "♥ ♠ ♣ ♦".split()
    
    nl = [["A", 1], ["K",10], ["Q",10], ["J",10]]
    
    # card counts
    nums = list(reversed(range(2,11)))
    [nl.append(l) for l in nums]

    # Create cards
    cards = list(map(list, it.product(suites, nl)))

    ##################### Still need to shuffle cards with random.shuffle which will change cards object in place
    
    # Make loop that grabs cards and disperses them to either the dealer or player
    deck_remaining = len(cards) + 1
    
    for count in range(0, deck_remaining, 4): # 4 cards drawn every time
        if len(cards) > 0:
            dealer_dealt1 = cards.pop()
            dealer_dealt2 = cards.pop()
            player_dealt1 = cards.pop()
            player_dealt2 = cards.pop()
            
            dd1_score = participant_score(dealer_dealt1)
            dd2_score = participant_score(dealer_dealt2)
            pd1_score = participant_score(player_dealt1)
            pd2_score = participant_score(player_dealt2)

            # Need to check if I'm trying to print out list, if I am, grab 1th element 
            # think about how to check both cards though
            ddl = []
            ddl_1 = []
            
            if type(dealer_dealt1) is list:
                for dl1 in dealer_dealt1:
                    if type(dl1) is list:
                        ddl = dl1[0] 
                        ddl_1 = dl1[1]
                        print("list:{}{}".format(dealer_dealt1[0],ddl))            
                else:
                    ddl = dealer_dealt1[0]
                    ddl_1 = dealer_dealt1[1]
                    print("not list: {}".format(ddl))
            
            # I am trying to print heart 
            print("D [{}]: {}{} {}{}".format(dd1_score+dd2_score, ddl, ddl_1, dealer_dealt2[0],dealer_dealt2[1]))
            print("P [{}]: {}{} {}{}".format(pd1_score+pd2_score, player_dealt1[0],player_dealt1[1], player_dealt2[0],player_dealt2[1]))
    
        
            # Game conditions:
            if dd1_score+dd2_score > 21:
                print("Dealer busts!")
                sys.exit(0)

            if pd1_score+pd2_score > 21:
                print("Player busts! You lose, loser!")
                sys.exit(0)

            if pd1_score+pd2_score == 21:
                print("Player wins. You probably cheated.") 
                sys.exit(0)

            if dd1_score+dd2_score == 21:
                print("Dealer wins!") 
                sys.exit(0)

            if dd1_score+dd2_score < 21:
                print("Dealer should hit")

            if pd1_score+pd2_score < 21:
                print("Player should hit")


# --------------------------------------------------
if __name__ == '__main__':
    main()

