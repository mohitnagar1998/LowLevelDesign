import random


class Dice:
    def __init__(self, dice_count: int = 1, min_face: int = 1, max_face: int = 6):
        self.dice_count = dice_count
        self.min_face = min_face
        self.max_face = max_face

    def roll_dice(self) -> int:
        total = 0
        for _ in range(self.dice_count):
            total += random.randint(self.min_face, self.max_face)
        return total
