from enums import City

class TheatreController:
    def __init__(self):
        self.theatres_by_city = {}
        self.all_theatres = []

    def add_theatre(self, theatre, city: City):
        self.all_theatres.append(theatre)
        self.theatres_by_city.setdefault(city, []).append(theatre)

    def get_all_shows(self, movie, city: City):
        theatre_vs_shows = {}
        theatres = self.theatres_by_city.get(city, [])

        for theatre in theatres:
            matching_shows = []
            for show in theatre.get_shows():
                if show.movie.get_movie_id() == movie.get_movie_id():
                    matching_shows.append(show)

            if matching_shows:
                theatre_vs_shows[theatre] = matching_shows

        return theatre_vs_shows
