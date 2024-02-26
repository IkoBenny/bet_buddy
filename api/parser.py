from bs4 import BeautifulSoup

#this function returns home and away player names.
def get_all_player_names(filename):
    stats = []
    with open(filename) as fp:
        soup = BeautifulSoup(fp, "html.parser")
    for tag in soup.find_all("a", class_="AnchorLink truncate db Boxscore__AthleteName"):
        for el in tag.contents:
            if not el.name == 'div' and not el.name == 'a' and not el.name == 'span':
                stats.append(el)
    return stats

#this function works identical to get_all_player_names(filename), with caveat that only away player names are returned. "amt" refers to the number of players listed on away team roster
def get_away_player_names(filename, amt):
    stats = []
    with open(filename) as fp:
        soup = BeautifulSoup(fp, "html.parser")
    for tag in soup.find_all("a", class_="AnchorLink truncate db Boxscore__AthleteName", limit = amt):
        for el in tag.contents:
            if not el.name == 'div' and not el.name == 'a' and not el.name == 'span':
                stats.append(el)
    return stats

#this function determines if a game finished in regular time.
def is_overtime_game(box):
    if box[6].isnumeric():
        return True
    else:
        return False

#this function utilizes Beautiful Soup API to parse an ESPN box score provided as HTML. It returns a list in CSV format. 
def parse_espn_box(filename):
    stats = []
    with open(filename) as fp:
        soup = BeautifulSoup(fp, "html.parser")
    for tag in soup.find_all("td", class_="Table__TD"):
        for el in tag.contents:
            if not el.name == 'div' and not el.name == 'a' and not el.name == 'span':
                stats.append(el)
    return stats