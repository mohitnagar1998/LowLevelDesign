from Game import Game
from Player import Player
from PlayingPiece import PieceType





if __name__ == "__main__":
    p1 = Player("mohit", PieceType.X)
    p2 = Player("divya", PieceType.O)
    game = Game(p1,p2, 3)
    game.start()