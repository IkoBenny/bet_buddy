from bs4 import BeautifulSoup

#this function returns home and away player names.
def get_all_player_names(soup):
    stats = []
    for tag in soup.find_all("a", class_="AnchorLink truncate db Boxscore__AthleteName"):
        for el in tag.contents:
            if not el.name == 'div' and not el.name == 'a' and not el.name == 'span':
                stats.append(el)
    return stats

#this function displays the box score for away team in CSV format.
def get_away_box_score(soup_obj):
    players = 0
    roster = []
    athlete = [] 
    for x in range(13, len(stats), 14):
        if x == 13:
            athlete = get_player_stats(stats, x)
            players = players + 1
            roster.append(athlete)
        else:
            if not get_player_stats(stats, x) == "done":
                athlete = get_player_stats(stats, x)
                players = players + 1
                roster.append(athlete)
            else:
                break
    counter2 = len(roster) * 14
    dnp =0
    while not get_player_dnp(stats, counter2) == "done":
        dnp = dnp + 1
        athlete = get_player_dnp(stats, counter2)
        roster.append(athlete)
        counter2 = counter2 + 1
        
    names = get_away_player_names(filename, len(roster))    
    for name, player in zip(names, roster):
         roster.append(name)      
    print(roster)

#this function displays the box score for both teams in CSV format.
def get_box_score(soup_obj):
    players = 0
    roster = []
    roster2 = []
    athlete = [] 
    dnp_home = 0
    dnp_away = 0
    away_players = 0
    home_players = 0
    
    stats = parse_espn_box(soup_obj)
    print(len(stats))
    
    if is_overtime_game(stats):
        print("ot")
    else:
        print("not ot")
        home = 0
        is_no_dnps_available = (len(stats) - 12) % 14 == 0
        if is_no_dnps_available:
            for x in range(12, len(stats), 14):
                if x == 12:
                    athlete = get_player_stats(stats, x)
                    players = players + 1
                    roster.append(athlete)
                else:
                    athlete = get_player_stats(stats, x)
                    players = players + 1
                    roster.append(athlete)
                    names = get_all_player_names(soup_obj)  
        else:
            print("dnps available for this game")   
            for x in range(12, len(stats), 14):
                if x == 12:
                    athlete = get_player_stats(stats, x)
                    players = players + 1
                    roster.append(athlete)
                else:
                    if not get_player_stats(stats, x) == "done":
                        athlete = get_player_stats(stats, x)
                        players = players + 1
                        roster.append(athlete)
                        home = x
                    else:
                        break
            counter2 = len(roster) * 14
            counter2 = counter2 + 12
            dnp =0
            print("stats: " + str(counter2))
            print("stats: " + str(stats[counter2]))
            print("before loop")
            while not get_player_dnp(stats, counter2) == "done":
                print("startloop")
                dnp = dnp + 1
                athlete = get_player_dnp(stats, counter2)
                roster.append(athlete)   
                counter2 = counter2 + 1
            dnp_away = dnp    
            print("after loop")
            is_home_no_dnps_available = home % 14 == 0 
            if is_home_no_dnps_available:
                for x in range(home + 14, len(stats), 14):
                    if x == home + 14:
                        athlete = get_player_stats(stats, x)
                        players = players + 1
                        roster.append(athlete)
                    else:
                        athlete = get_player_stats(stats, x)
                        players = players + 1
                        roster.append(athlete)
                    print("home: " + stats[home])
            else:
                print("dnps available for home")
                print("home: " + stats[home])
                dnp_away_count = 0
                for x in range(home, home + 50 , 1):
                    if stats[x] == "DNP-COACH'S DECISION":
                        dnp_away_count = dnp_away_count + 1
                print("dnp: " + str(dnp_away_count))
                for x in range(home + dnp_away_count + 14, len(stats), 14):
                    if x == home + dnp_away_count + 14:
                        print("expected" + stats[home])
                        athlete = get_player_stats(stats, x)
                        players = players + 1
                        roster2.append(athlete)
                    else:
                        if not get_player_stats(stats, x) == "done":
                            athlete = get_player_stats(stats, x)
                            players = players + 1
                            roster2.append(athlete)
                            home = x
                        else:
                            break
            counter2 = len(roster2) * 14
            counter2 = counter2 + 12
            dnp =0
            print("stats: " + str(counter2))
            print("stats: " + str(stats[counter2]))
            print("before loop")
            while not get_player_dnp(stats, counter2) == "done":
                print("startloop")
                dnp = dnp + 1
                athlete = get_player_dnp(stats, counter2)
                roster2.append(athlete)   
                counter2 = counter2 + 1
            print("after loop")
            dnp_away = dnp   
        if is_no_dnps_available:
            for name, player in zip(names, roster):
                roster.append(name) 
        else:
            print("dnps available for this game")
            home_players = len(roster)
            away_players = len(roster2)
            names = get_all_player_names(soup_obj)
            names_played = []
            for x in range(0, away_players):
                names_played.append(names[x])
            for x in range(away_players, len(names)):
                names_played.append(names[x])
            
    roster.append(roster2)
    for name, player in zip(names_played, roster):
        roster.append(name) 
    print(names_played)
    print(roster)
    print("x: " + str(home))
    print("test")


#this function works identical to get_all_player_names(filename), with caveat that only away player names are returned. "amt" refers to the number of players listed on away team roster
def get_away_player_names(soup, amt):
    stats = []
    for tag in soup.find_all("a", class_="AnchorLink truncate db Boxscore__AthleteName", limit = amt):
        for el in tag.contents:
            if not el.name == 'div' and not el.name == 'a' and not el.name == 'span':
                stats.append(el)
    return stats

#this function returns the final values for all quarters including OT.
def get_overtime_totals_by_quarter(box):
    stats = []
    for key, value in zip(overtime_values_periods.keys(), overtime_values_periods.values()):
        stats.append(str(key) + ", " + str(box[value]))
    return stats

#this function determines if a game finished in regular time.
def is_overtime_game(box):
    if box[6].isnumeric():
        return True
    else:
        return False

#this helper-function is executed whenever get_away_box_score(filename, stats) is called. 
def get_player_dnp(box, counter):
    if box[counter] == "DNP-COACH'S DECISION":
        return "DNP-COACH'S DECISION"
    else:
        return "done"

#this function parses a box score row. It returns a list in CSV format. 
def get_player_stats(box, counter):
    stats = []
    for key, value in zip(player.keys(), player.values()):
        if not box[value + counter] == "DNP-COACH'S DECISION":
            stats.append(key + ", " + str(box[value + counter]))
        else:
            return "done"
    return stats



#this function utilizes Beautiful Soup API to parse an ESPN box score provided as HTML. It returns a list in CSV format. 
def parse_espn_box(soup):
    stats = []
    for tag in soup.find_all("td", class_="Table__TD"):
        for el in tag.contents:
            if not el.name == 'div' and not el.name == 'a' and not el.name == 'span':
                stats.append(el)
    return stats