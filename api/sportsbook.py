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
def get_moneyline_winner_from_box_first(stats):
    if not is_overtime_game(stats):
        if int(stats[normal_time_values_periods.a_first]) > int(stats[normal_time_values_periods.h_first]):
            print(stats[normal_time_values_periods.away] + " - 1ST QTR MONEYLINE: YES")
            print(stats[normal_time_values_periods.h] + " - 1ST QTR MONEYLINE: NO")
        else:
            if int(stats[normal_time_values_periods.a_first]) < int(stats[normal_time_values_periods.h_first]):
                print(stats[normal_time_values_periods.away] + " - 1ST QTR MONEYLINE: NO")
                print(stats[normal_time_values_periods.h] + " - 1ST QTR MONEYLINE: YES")
            else:
                print("1ST QTR MONEYLINE: TIE")
    else:
        if int(stats[overtime_values_periods.a_first]) > int(stats[overtime_values_periods.h_first]):
            print(stats[overtime_values_periods.away] + " - 1ST QTR MONEYLINE: YES")
            print(stats[overtime_values_periods.h] + " - 1ST QTR MONEYLINE: NO")
        else:
            if int(stats[overtime_values_periods.a_first]) < int(stats[overtime_values_periods.a_first]):
                print(stats[overtime_values_periods.away] + " - 1ST QTR MONEYLINE: YES")
                print(stats[overtime_values_periods.h] + " - 1ST QTR MONEYLINE: NO")
            else:
                print("1ST QTR MONEYLINE: TIE")
    
#this function determines the second quarter 3-way ML winner.    
def get_moneyline_winner_from_box_second(stats):
    if not is_overtime_game(stats):
        if int(stats[normal_time_values_periods.a_second]) > int(stats[normal_time_values_periods.h_second]):
            print(stats[normal_time_values_periods.away] + " - 2ND QTR MONEYLINE: NO")
            print(stats[normal_time_values_periods.h] + " - 2ND QTR MONEYLINE: YES")
        else:
            if int(stats[normal_time_values_periods.a_second]) < int(stats[normal_time_values_periods.h_second]):
                print(stats[normal_time_values_periods.away] + " - 2ND QTR MONEYLINE: NO")
                print(stats[normal_time_values_periods.h] + " - 2ND QTR MONEYLINE: YES")
            else:
                print("2ND QTR MONEYLINE: TIE")
    else:
        if int(stats[overtime_values_periods.a_second]) > int(stats[overtime_values_periods.h_second]):
            print(stats[overtime_values_periods.away] + " - 2ND QTR MONEYLINE: YES")
            print(stats[overtime_values_periods.h] + " - 2ND QTR MONEYLINE: NO")
        else:
            if int(stats[overtime_values_periods.a_second]) < int(stats[overtime_values_periods.h_second]):
                print(stats[overtime_values_periods0] + " - 2ND QTR MONEYLINE: YES")
                print(stats[overtime_values_periods7] + " - 2ND QTR MONEYLINE: NO")
            else:
                print("2ND QTR MONEYLINE: TIE")

#this function determines the third quarter 3-way ML winner.             
def get_moneyline_winner_from_box_third(stats):
    if not is_overtime_game(stats):
        if int(stats[normal_time_values_periods.a_third]) > int(stats[normal_time_values_periods.h_third]):
            print(stats[normal_time_values_periods.away] + " - 3RD QTR MONEYLINE: NO")
            print(stats[normal_time_values_periods.h] + " - 3RD QTR MONEYLINE: YES")
        else:
            if int(stats[normal_time_values_periods.a_third]) < int(stats[normal_time_values_periods.h_third]):
                print(stats[normal_time_values_periods.away] + " - 3RD QTR MONEYLINE: NO")
                print(stats[normal_time_values_periods.h] + " - 3RD QTR MONEYLINE: YES")
            else:
                print("3RD QTR MONEYLINE: TIE")
    else:
        if int(stats[overtime_values_periods.a_third]) > int(stats[overtime_values_periods.h_third]):
            print(stats[overtime_values_periods.away] + " - 3RD QTR MONEYLINE: YES")
            print(stats[overtime_values_periods.h] + " - 3RD QTR MONEYLINE: NO")
        else:
            if int(stats[overtime_values_periods.a_third]) < int(stats[overtime_values_periods.h_third]):
                print(stats[overtime_values_periods.away] + " - 3RD QTR MONEYLINE: YES")
                print(stats[overtime_values_periods.h] + " - 3RD QTR MONEYLINE: NO")
            else:
                print("3RD QTR MONEYLINE: TIE")

#this function determines the match ML winner.
def get_moneyline_winner_from_box(stats):
    if not is_overtime_game(stats):
        if int(stats[normal_time_values_periods.a_total]) > int(stats[normal_time_values_periods.h_total]):
            print(stats[normal_time_values_periods.away] + " - MONEYLINE: NO")
            print(stats[normal_time_values_periods.h] + " - MONEYLINE: YES")
        else:
            print(stats[normal_time_values_periods.away] + " - MONEYLINE: YES")
            print(stats[normal_time_values_periods.h] + " - MONEYLINE: NO")
    else:
        if int(stats[overtime_values_periods.a_ot]) > int(stats[overtime_values_periods.h_ot]):
            print(stats[overtime_values_periods.away] + " - MONEYLINE: YES")
            print(stats[overtime_values_periods.home] + " - MONEYLINE: NO")
        else:
            print(stats[overtime_values_periods.away] + " - MONEYLINE: YES")
            print(stats[overtime_values_periods.home] + " - MONEYLINE: NO")