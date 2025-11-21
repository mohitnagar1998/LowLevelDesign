from ElevatorState import ElevatorState
from Direction import Direction
from InternalButtons import InternalButtons
from ElevatorDoor import ElevatorDoor
from ElevatorDisplay import ElevatorDisplay


class ElevatorCar:
    def __init__(self):
        self.id = 0
        self.display = ElevatorDisplay()
        self.internal_buttons = InternalButtons()
        self.elevator_state = ElevatorState.IDLE
        self.current_floor = 0
        self.elevator_direction = Direction.UP
        self.elevator_door = ElevatorDoor()

    def show_display(self):
        return self.display.show_display()

    def press_button(self, destination):
        self.internal_buttons.press_buttons(destination, self)

    def set_display(self):
        self.display.set_display(self.current_floor, self.elevator_direction)

    def move_elevator(self, destination_floor: int) -> bool:
        # simple move logic: set current_floor to destination and display intermediate states
        start_floor = self.current_floor
        if destination_floor == start_floor:
            print(f"[elevator {self.id}] already at floor {destination_floor}")
            return True

        # set destination
        if destination_floor > start_floor:
            self.elevator_direction = Direction.UP
            step = 1
        else:
            self.elevator_direction = Direction.DOWN
            step = -1

        self.elevator_state = ElevatorState.MOVING

        # simulate moving floor by floor (instantaneous for demo)
        print(f"[elevator {self.id}] moving from {start_floor} to {destination_floor} ({self.elevator_direction})")
        for f in range(start_floor + step, destination_floor + step, step):
            self.current_floor = f
            self.set_display()
            self.show_display()

        # arrived
        self.elevator_state = ElevatorState.IDLE

        # open/close door
        self.elevator_door.open_door()
        self.elevator_door.close_door()
        return True