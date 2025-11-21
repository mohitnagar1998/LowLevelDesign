from ElevatorRegistry import elevator_controller_list
from ElevatorCar import ElevatorCar


class InternalDispatcher:
    def __init__(self):
        self.elevator_controller_list = elevator_controller_list

    def submit_internal_request(self, floor: int, elevator_car: ElevatorCar):
        for elevator_controller in self.elevator_controller_list:
            if elevator_controller.elevator_car is elevator_car:
                elevator_controller.submit_internal_request(floor)
                return

        print(f"internal dispatcher: elevator car not found for internal request")
