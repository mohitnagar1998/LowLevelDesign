class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]
        self.moves = 0

    def add_piece(self, x, y, mark):
        try:
            if x > self.size or y > self.size:
                print("index out of range")
                return False
            if self.board[x][y] is not None:
                print("position already occupied")
                return False

            self.board[x][y] = mark
            self.moves += 1

        except Exception as e:
            print(f"an error occurred --> {e}")

    def is_full(self):
        return self.moves == self.size * self.size

    def print_board(self):
        for row in self.board:
            print([cell.value if cell else "-" for cell in row])
        print()
