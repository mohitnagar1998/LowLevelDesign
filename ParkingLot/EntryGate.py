from ParkingSpotManager import ParkingSpotManagerFactory


class Entrance:
    def __init__(self, vehicle_type):
        self.parking_spot_factory = ParkingSpotManagerFactory.allot_parking_spot(vehicle_type)


    def find_space(self, entry_gate):
        pass

    def book_spot(self):
        pass

    def generate_ticket(self):
        pass
