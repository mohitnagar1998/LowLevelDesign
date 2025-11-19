from Game import Game


if __name__ == "__main__":
    game = Game()
    print("starting game with board and random snakes and ladders.")

    jumps = []
    board_length = len(game.board.cells)
    for r in range(board_length):
        for c in range(board_length):
            pos = r * board_length + c
            cell = game.board.cells[r][c]
            if cell.jump:
                jumps.append((pos, cell.jump))
    print(f"placed jumps (start -> end): {jumps}")

    game.start_game()