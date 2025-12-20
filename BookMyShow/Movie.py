class Movie:
    def __init__(self):
        self.movie_id = None
        self.movie_name = None
        self.movie_duration_in_minutes = None

    def get_movie_id(self):
        return self.movie_id

    def set_movie_id(self, movie_id):
        self.movie_id = movie_id

    def get_movie_name(self):
        return self.movie_name

    def set_movie_name(self, movie_name):
        self.movie_name = movie_name

    def get_movie_duration(self):
        return self.movie_duration_in_minutes

    def set_movie_duration(self, duration):
        self.movie_duration_in_minutes = duration
