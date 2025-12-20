class Show:
    def __init__(self):
        self.show_id = None
        self.movie = None
        self.screen = None
        self.show_start_time = None
        self.booked_seat_ids = []

    def get_booked_seat_ids(self):
        return self.booked_seat_ids