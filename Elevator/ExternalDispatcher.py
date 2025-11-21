from ElevatorRegistry import elevator_controller_list
from Direction import Direction

class ExternalDispatcher:
    def __init__(self):
        self.elevator_controller_list = elevator_controller_list

    def submit_external_request(self, floor: int, direction: Direction):
        # simple distribution -> odd floors - odd elevator ids, even floor - even elevator ids
        for elevator_controller in self.elevator_controller_list:
            elevator_id = elevator_controller.elevator_car.id
            if elevator_id % 2 == 0 and floor % 2 == 0:
                elevator_controller.submit_external_request(floor, direction)
            else:
                elevator_controller.submit_external_request(floor, direction)
            print(f"[external_dispatcher] assigning floor {floor} to elevator {elevator_id}")

