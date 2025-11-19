from Vehicle import Vehicle
from abc import ABC, abstractmethod


class ParkingSpot(ABC):
    def __init__(self, spot_id, price):
        self.parking_spot_id = spot_id
        self.price = price
        self.is_occupied = False
        self.vehicle = None
    def park_vehicle(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def unpark_vehicle(self):
        vehicle = self.vehicle
        self.is_occupied = True
        self.vehicle = None
        return vehicle

    @abstractmethod
    def price(self):
        pass


class TwoWheelerParkingSpot(ParkingSpot):
    def price(self):
        pass


class ThreeWheelerParkingSpot(ParkingSpot):
    def price(self):
        pass
