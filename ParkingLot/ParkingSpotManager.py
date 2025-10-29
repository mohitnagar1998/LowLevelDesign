from abc import ABC, abstractmethod
from Vehicle import VehicleType
from ParkingSpot import TwoWheelerParkingSpot, ThreeWheelerParkingSpot
from typing import List


class ParkingSpotManager(ABC):

    @abstractmethod
    def find_parking_space(self):
        pass

    @abstractmethod
    def add_parking_space(self):
        pass

    @abstractmethod
    def remove_parking_space(self):
        pass

    @abstractmethod
    def park_vehicle(self):
        pass

    @abstractmethod
    def remove_vehicle(self):
        pass


class TwoWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self):
        self.list_of_two_wheeler_parking_spot = List[TwoWheelerParkingSpot]

    def find_parking_space(self):
        pass

    def add_parking_space(self):
        pass

    def remove_parking_space(self):
        pass

    def park_vehicle(self):
        pass

    def remove_vehicle(self):
        pass


class ThreeWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self):
        self.list_of_three_wheeler_parking_spot = List[ThreeWheelerParkingSpot]

    def find_parking_space(self):
        pass

    def add_parking_space(self):
        pass

    def remove_parking_space(self):
        pass

    def park_vehicle(self):
        pass

    def remove_vehicle(self):
        pass


class ParkingSpotManagerFactory:
    def allot_parking_spot(self, vehicle_type):
        if vehicle_type == VehicleType.TwoWheeler:
            return TwoWheelerParkingSpotManager()

        if vehicle_type == VehicleType.FourWheeler:
            return ThreeWheelerParkingSpotManager()

        else:
            return "invalid vehicle type"
