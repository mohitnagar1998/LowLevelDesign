class MovieController:
    def __init__(self):
        self.movies_by_city = {}  # city -> List[Movie]
        self.all_movies = []