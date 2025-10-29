from PlayingPiece import PieceType


class Player:
    def __init__(self, name, piece: PieceType):
        self.player_name = name
        self.playing_piece = piece

