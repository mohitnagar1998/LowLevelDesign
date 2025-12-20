# main runner file
from enums import City, SeatCategory
from Movie import Movie
from Seat import Seat
from Screen import Screen
from Show import Show
from Theatre import Theatre
from Booking import Booking
from MovieController import MovieController
from TheatreController import TheatreController


class BookMyShow:
    def __init__(self):
        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()

    def initialize(self):
        self.create_movies()
        self.create_theatre()

    def create_booking(self, user_city, movie_name):
        movies = self.movie_controller.get_movie_by_city(user_city)
        interested_movie = next((m for m in movies if m.get_movie_name() == movie_name), None)

        if not interested_movie:
            print("movie not available in this city")
            return

        shows_map = self.theatre_controller.get_all_shows(interested_movie, user_city)
        theatre, shows = next(iter(shows_map.items()))
        interested_show = shows[0]

        seat_number = 30
        if seat_number not in interested_show.get_booked_seat_ids():
            interested_show.get_booked_seat_ids().append(seat_number)

            booking = Booking()
            booked_seats = [
                seat for seat in interested_show.screen.get_seats()
                if seat.get_seat_id() == seat_number
            ]

            booking.set_show(interested_show)
            booking.set_booked_seats(booked_seats)
            print("BOOKING SUCCESSFUL")
        else:
            print("seat already booked")

    def create_theatre(self):
        avengers = self.movie_controller.get_movie_by_name("AVENGERS")
        baahubali = self.movie_controller.get_movie_by_name("BAAHUBALI")

        inox = Theatre()
        inox.theatre_id = 1
        inox.city = City.Bangalore
        inox.set_screens(self.create_screens())

        inox.shows = [
            self.create_show(1, inox.screens[0], avengers, 8),
            self.create_show(2, inox.screens[0], baahubali, 16)
        ]

        self.theatre_controller.add_theatre(inox, City.Bangalore)

    def create_movies(self):
        avengers = Movie()
        avengers.set_movie_id(1)
        avengers.set_movie_name("AVENGERS")
        avengers.set_movie_duration(128)

        baahubali = Movie()
        baahubali.set_movie_id(2)
        baahubali.set_movie_name("BAAHUBALI")
        baahubali.set_movie_duration(180)

        self.movie_controller.add_movie(avengers, City.Bangalore)
        self.movie_controller.add_movie(baahubali, City.Bangalore)

    def create_screens(self):
        screen = Screen()
        screen.set_screen_id(1)
        screen.set_seats(self.create_seats())
        return [screen]

    def create_show(self, show_id, screen, movie, start_time):
        show = Show()
        show.show_id = show_id
        show.screen = screen
        show.movie = movie
        show.show_start_time = start_time
        return show

    def create_seats(self):
        seats = []
        for i in range(0, 40):
            seat = Seat()
            seat.set_seat_id(i)
            seat.set_seat_category(SeatCategory.SILVER)
            seats.append(seat)

        for i in range(40, 70):
            seat = Seat()
            seat.set_seat_id(i)
            seat.set_seat_category(SeatCategory.GOLD)
            seats.append(seat)

        for i in range(70, 100):
            seat = Seat()
            seat.set_seat_id(i)
            seat.set_seat_category(SeatCategory.PLATINUM)
            seats.append(seat)

        return seats


if __name__ == "__main__":
    app = BookMyShow()
    app.initialize()
    app.create_booking(City.Bangalore, "BAAHUBALI")
    app.create_booking(City.Bangalore, "BAAHUBALI")
