from ParkingSpot import ParkingSpot
from abc import ABC, abstractmethod



class ParkingSpotManager(ABC):
    def __init__(self):
        self.parking_spots = {}

    def find_parking_space(self, vehicle):
        for spot in self.parking_spots.values():
            if not spot.is_occupied:
                return spot
        return None

    def add_parking_spot(self, parking_spot):
        self.parking_spots[parking_spot.spot_id] = parking_spot

    # def parkVehicle(self):
    #     pass
    #
    # def unparkVehicle(self):
    #     pass


class TwoWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self):
        super().__init__()

class FourWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self):
        super().__init__()


class ParkingSpotManagerFactory:

    def getParkingManager(self, parkingType):
        if parkingType.lower() == "twowheeler":
            return TwoWheelerParkingSpotManager()

        elif parkingType.lower() == "fourwheeler":
            return FourWheelerParkingSpotManager()

        else:
            return "invalid parking type"
