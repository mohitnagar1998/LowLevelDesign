from InternalDispatcher import InternalDispatcher
from ElevatorCar import ElevatorCar



class InternalButtons:
    def __init__(self):
        self.dispatcher = InternalDispatcher()
        self.available_buttons = list(range(1, 11))
        self.buttons_selected = None

    def press_buttons(self, destination: int, elevator_car: ElevatorCar):
        print(f"[InternalButtons] buttons pressed for destination {destination} in elevator {elevator_car.id}")
        self.dispatcher.submit_internal_request(destination, elevator_car)