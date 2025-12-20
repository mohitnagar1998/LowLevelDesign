from enums import City

class MovieController:
    def __init__(self):
        self.movies_by_city = {}  # city -> List[Movie]
        self.all_movies = []

    def add_movie(self, movie, city: City):
        self.all_movies.append(movie)
        self.movies_by_city.setdefault(city, []).append(movie)

    def get_movie_by_name(self, name):
        for movie in self.all_movies:
            if movie.get_movie_name() == name:
                return movie
        return None

    def get_movie_by_city(self, city: City):
        return self.movies_by_city.get(city, [])
