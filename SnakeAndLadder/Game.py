from Board import Board
from Dice import Dice
from Player import Player
from typing import Optional
from collections import deque

class Game:
    def __init__(self):
        self.board: Optional[Board] = None
        self.dice: Optional[Dice] = None
        self.player_list: deque[Player] = deque()
        self.winner: Optional[Player] = None
        self.initialize_game()

    def initialize_game(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self.add_players()

    def add_players(self):
        player1 = Player("p1", 0)
        player2 = Player("p2", 0)
        self.player_list.append(player1)
        self.player_list.append(player2)

    def start_game(self):
        final_index = len(self.board.cells) * len(self.board.cells) - 1
        while self.winner is None:
            player_turn = self.find_player_turn()
            print(f"player turn is: {player_turn.id} current position is {player_turn.current_position}")
            dice_numbers = self.dice.roll_dice()
            player_new_position = player_turn.current_position + dice_numbers
            player_new_position = self.jump_check(player_new_position)
            player_turn.current_position = player_new_position
            print(f"player turn is: {player_turn.id} new position is {player_turn.current_position}")
            if player_new_position >= final_index:
                self.winner = player_turn

    def find_player_turn(self) -> Player:
        player_turns = self.player_list.popleft()
        self.player_list.append(player_turns)
        return player_turns

    def jump_check(self, player_new_position: int) -> int:
        final_index = len(self.board.cells) * len(self.board.cells) - 1
        if player_new_position > final_index: return player_new_position
        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jump_by = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print(f"jump done by: {jump_by}")
            return cell.jump.end
        else:
            return player_new_position