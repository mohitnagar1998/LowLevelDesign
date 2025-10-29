from abc import ABC, abstractmethod
import PricingStrategy
from Vehicle import VehicleType

class CostComputation(ABC):
    @abstractmethod
    def price(self):
        pass

class TwoWheelerCostComputation(CostComputation):
    def price(self):
        pass


class ThreeWheelerCostComputation(CostComputation):
    def price(self):
        pass


class CostComputationFactory:
    def compute_cost(self, ticket):
        if ticket.vehicle_type == VehicleType.TwoWheeler:
            pass

        elif ticket.vehicle_type == VehicleType.FourWheeler:
            pass

        else:
            return "invalid ticket"