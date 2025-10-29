from datetime import time
from Vehicle import VehicleType


class Ticket:
    def __init__(self):
        self.entry_time = time()
        self.vehicle_type = VehicleType
        self.parking_spot = None

    def get_vehicle_type(self):
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
