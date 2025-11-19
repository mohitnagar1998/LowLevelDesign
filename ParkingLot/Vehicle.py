from enum import Enum


class VehicleType(Enum):
    CAR = 1
    BIKE = 2


class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
