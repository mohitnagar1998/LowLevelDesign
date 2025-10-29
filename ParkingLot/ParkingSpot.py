from abc import ABC, abstractmethod
from Vehicle import Vehicle
from Ticket import Ticket

class ParkingSpot(ABC):
    def __init__(self):
        self.id: int
        self.isEmpty: bool
        self.vehicle: Vehicle


    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def park_vehicle(self):
        pass

    @abstractmethod
    def remove_vehicle(self):
        pass


class TwoWheelerParkingSpot(ParkingSpot):
    def price(self):
        print("two wheeler parking spot price")

    def park_vehicle(self):
        pass

    def remove_vehicle(self):
        pass

class ThreeWheelerParkingSpot(ParkingSpot):
    def price(self):
        print("three wheeler parking spot price")

    def park_vehicle(self):
        pass

    def remove_vehicle(self):
        pass

