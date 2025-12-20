from enums import SeatCategory

class Seat:
    def __init__(self):
        self.seat_id = None
        self.seat_row = None
        self.seat_category = None

    def get_seat_id(self):
        return self.seat_id

    def set_seat_id(self, seat_id):
        self.seat_id = seat_id

    def get_row(self):
        return self.seat_row

    def set_row(self, row):
        self.seat_row = row

    def get_seat_category(self):
        return self.seat_category

    def set_seat_category(self, seat_category: SeatCategory):
        self.seat_category = seat_category
