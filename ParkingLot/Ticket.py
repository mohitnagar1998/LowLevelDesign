from datetime import datetime


class Ticket:
    def __init__(self, vehicle, parking_spot):
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = datetime.now()
        self.exit_time = None

    def set_exit_time(self):
        self.exit_time = datetime.now()