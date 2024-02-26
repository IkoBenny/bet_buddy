from bs4 import BeautifulSoup
from model import *

#this function determines the first quarter/match ML winner.
def get_moneyline_and_first_quarter_winner_from_box(stats):
    if not is_overtime_game(stats):
        if int(stats[1]) > int(stats[7]) and int(stats[5]) > int(stats[11]):
            print(stats[0] + " - FIRST QUARTER WINNER / MATCH WINNER: YES")
            print(stats[6] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")
        else:
            if int(stats[1]) < int(stats[7]) and int(stats[5]) < int(stats[11]):
                print(stats[0] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")
                print(stats[6] + " - FIRST QUARTER WINNER / MATCH WINNER: YES")
            else:
                print(stats[0] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")
                print(stats[6] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")    
    else:
        if int(stats[1]) > int(stats[8]) and int(stats[6]) > int(stats[12]):
            print(stats[0] + " - FIRST QUARTER WINNER / MATCH WINNER: YES")
            print(stats[7] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")
        else:
            if int(stats[1]) < int(stats[8]) and int(stats[6]) < int(stats[12]):
                print(stats[0] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")
                print(stats[7] + " - FIRST QUARTER WINNER / MATCH WINNER: YES")
            else:
                print(stats[0] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")
                print(stats[7] + " - FIRST QUARTER WINNER / MATCH WINNER: NO")

#this function determines the first quarter 3-way ML winner.
def get_first_moneyline_winner_from_box(stats):
    if not is_overtime_game(stats):
        if int(stats[1]) > int(stats[7]):
            print(stats[0] + " - 1ST QTR MONEYLINE: YES")
            print(stats[6] + " - 1ST QTR MONEYLINE: NO")
        else:
            if int(stats[1]) < int(stats[7]):
                print(stats[0] + " - 1ST QTR MONEYLINE: NO")
                print(stats[6] + " - 1ST QTR MONEYLINE: YES")
            else:
                print("1ST QTR MONEYLINE: TIE")
    else:
        if int(stats[1]) > int(stats[8]):
            print(stats[0] + " - 1ST QTR MONEYLINE: YES")
            print(stats[7] + " - 1ST QTR MONEYLINE: NO")
        else:
            if int(stats[1]) < int(stats[8]):
                print(stats[0] + " - 1ST QTR MONEYLINE: YES")
                print(stats[7] + " - 1ST QTR MONEYLINE: NO")
            else:
                print("1ST QTR MONEYLINE: TIE")
    
#this function determines the second quarter 3-way ML winner.    
def get_second_moneyline_winner_from_box(stats):
    if not is_overtime_game(stats):
        if int(stats[2]) > int(stats[8]):
            print(stats[0] + " - 2ND QTR MONEYLINE: NO")
            print(stats[6] + " - 2ND QTR MONEYLINE: YES")
        else:
            if int(stats[2]) < int(stats[8]):
                print(stats[0] + " - 2ND QTR MONEYLINE: NO")
                print(stats[6] + " - 2ND QTR MONEYLINE: YES")
            else:
                print("2ND QTR MONEYLINE: TIE")
    else:
        if int(stats[2]) > int(stats[9]):
            print(stats[0] + " - 2ND QTR MONEYLINE: YES")
            print(stats[7] + " - 2ND QTR MONEYLINE: NO")
        else:
            if int(stats[2]) < int(stats[9]):
                print(stats[0] + " - 2ND QTR MONEYLINE: YES")
                print(stats[7] + " - 2ND QTR MONEYLINE: NO")
            else:
                print("2ND QTR MONEYLINE: TIE")

#this function determines the third quarter 3-way ML winner.             
def get_third_moneyline_winner_from_box(stats):
    if not is_overtime_game(stats):
        if int(stats[3]) > int(stats[9]):
            print(stats[0] + " - 3RD QTR MONEYLINE: NO")
            print(stats[6] + " - 3RD QTR MONEYLINE: YES")
        else:
            if int(stats[3]) < int(stats[9]):
                print(stats[0] + " - 3RD QTR MONEYLINE: NO")
                print(stats[6] + " - 3RD QTR MONEYLINE: YES")
            else:
                print("2ND QTR MONEYLINE: TIE")
    else:
        if int(stats[3]) > int(stats[10]):
            print(stats[0] + " - 3RD QTR MONEYLINE: YES")
            print(stats[7] + " - 3RD QTR MONEYLINE: NO")
        else:
            if int(stats[3]) < int(stats[10]):
                print(stats[0] + " - 3RD QTR MONEYLINE: YES")
                print(stats[7] + " - 3RD QTR MONEYLINE: NO")
            else:
                print("3RD QTR MONEYLINE: TIE")

#this function determines the match ML winner.
def get_moneyline_winner_from_box(stats):
    if not is_overtime_game(stats):
        if int(stats[5]) > int(stats[11]):
            print(stats[0] + " - MONEYLINE: NO")
            print(stats[6] + " - MONEYLINE: YES")
        else:
            print(stats[0] + " - MONEYLINE: YES")
            print(stats[6] + " - MONEYLINE: NO")
    else:
        if int(stats[5]) > int(stats[11]):
            print(stats[0] + " - MONEYLINE: YES")
            print(stats[7] + " - MONEYLINE: NO")
        else:
            print(stats[0] + " - MONEYLINE: YES")
            print(stats[7] + " - MONEYLINE: NO")