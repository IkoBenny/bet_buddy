class soup:
    def __init__(self, filename):
        self.soup_obj = get_soup(filename)
    
    #this function returns the Beautiful Soup object.
    def get_soup(filename):
        with open(filename) as fp:
            soup = BeautifulSoup(fp, "html.parser")
            return soup