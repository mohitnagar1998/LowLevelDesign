from Cell import Cell
from Jump import Jump
import random
class Board:
    def __init__(self, board_size: int, number_of_snakes: int, number_of_ladders: int):
        self.cells = [[Cell() for _ in range(board_size)] for _ in range(board_size)]
        self.add_snakes_ladders(number_of_snakes, number_of_ladders)

    def add_snakes_ladders(self, number_of_snakes: int, number_of_ladders: int):
        cells = len(self.cells) * len(self.cells)
        attemps = 0

        while number_of_snakes > 0 and attemps < number_of_snakes * 50:
            start = random.randrange(1, cells - 1)
            end = random.randrange(1, cells - 1)


            if end < start:
                jump_obj = Jump(start, end)
                cell = self.get_cell(start)
                if cell.jump is None:
                    cell.jump = jump_obj
                    number_of_snakes -= 1

            attemps += 1

        while number_of_ladders > 0 and attemps < number_of_ladders * 50:
            start = random.randrange(1, cells - 1)
            end = random.randrange(1, cells - 1)

            if end > start:
                jump_obj = Jump(start, end)
                cell = self.get_cell(start)
                if cell.jump is None:
                    cell.jump = jump_obj
                    number_of_snakes -= 1

            attemps += 1

    def get_cell(self, player_position: int) -> Cell:
        row = player_position // len(self.cells)
        col = player_position % len(self.cells)
        return self.cells[row][col]