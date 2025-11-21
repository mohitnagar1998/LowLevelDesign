from Direction import Direction


class ElevatorDisplay:
    def __init__(self):
        self.floor = 0
        self.direction = Direction.UP

    def set_display(self, floor: int, direction: Direction):
        self.floor = floor
        self.direction = direction

    def show_display(self):
        print(f"display -> floor: {self.floor}, direction: {self.direction}")
        