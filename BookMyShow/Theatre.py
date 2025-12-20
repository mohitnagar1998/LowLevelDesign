class Theatre:
    def __init__(self):
        self.theatre_id = None
        self.address = None
        self.city = None
        self.screens = []
        self.shows = []


    def get_shows(self):
        return self.shows

    def set_shows(self, shows):
        self.shows = shows

    def get_screens(self):
        return self.screens

    def set_screens(self, screens):
        self.screens = screens
