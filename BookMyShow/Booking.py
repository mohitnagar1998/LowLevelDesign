class Booking:
    def __init__(self):
        self.show = None
        self.booked_seats = []
        self.payment = None

    def set_show(self, show):
        self.show = show

    def set_booked_seats(self, seats):
        self.booked_seats = seats

    def set_payment(self, payment):
        self.payment = payment