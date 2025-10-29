from enum import Enum


class VehicleType(Enum):
    TwoWheeler = 1
    FourWheeler = 2


class Vehicle:
    def __init__(self):
        self.vehicle_number = int()
        self.vehicle_type = VehicleType
