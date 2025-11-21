from ElevatorController import ElevatorController
from ElevatorCar import ElevatorCar
from ElevatorRegistry import elevator_controller_list


def _init_elevators():
    # create two elevator cars and controllers
    elevator_car1 = ElevatorCar()
    elevator_car1.id = 1
    controller1 = ElevatorController(elevator_car1)

    elevator_car2 = ElevatorCar()
    elevator_car2.id = 2
    controller2 = ElevatorController(elevator_car2)

    elevator_controller_list.append(controller1)
    elevator_controller_list.append(controller2)


# initialize at import
_init_elevators()
