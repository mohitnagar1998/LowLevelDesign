from enum import Enum


class ElevatorState(Enum):
    MOVING = 1
    IDLE = 2

    def __str__(self):
        return "MOVING" if self == ElevatorState.MOVING else "IDLE"
