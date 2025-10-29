from Board import Board


class Game:
    def __init__(self, player_1, player_2, size):
        self.board = Board(size)
        self.players = [player_1, player_2]
        self.current = 0
        self.size = size
        self.state = "IN_PROGRESS"

        # counters for 0(1) win check
        self.rows = [[0] * size for _ in range(2)]
        self.cols = [[0] * size for _ in range(2)]
        self.diag = [0, 0]
        self.anti_diag = [0, 0]

    def play_move(self, x, y):
        player = self.players[self.current]
        self.board.add_piece(x, y, player.playing_piece)

        idx =self.current
        n = self.size
        self.rows[idx][x] += 1
        self.cols[idx][y] += 1

        if x == y:
            self.diag[idx] += 1

        if x + y == n - 1:
            self.anti_diag[idx] += 1

        #Check Winner
        if (self.rows[idx][x] == n or self.cols[idx][y] == n or
                self.diag[idx] == n or self.anti_diag[idx] == n):
            self.state = f"{player.name} wins!"
            return self.state

        if self.board.is_full():
            self.state = "Draw"
            return self.state

        self.current = 1 - self.current
        return "Next move"

    def start(self):
        while self.state == "IN_PROGRESS":
            self.board.print_board()
            player = self.players[self.current]
            print(f"{player.player_name}'s turn ({player.playing_piece.value})")
            r = int(input("Row: "))
            c = int(input("Col: "))
            try:
                result = self.play_move(r, c)
                print(result)
            except ValueError as e:
                print(e)
        self.board.print_board()
        print("Game Over:", self.state)
