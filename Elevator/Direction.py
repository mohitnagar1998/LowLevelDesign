from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = -1

    def __str__(self):
        return "UP" if self == Direction.UP else "DOWN"