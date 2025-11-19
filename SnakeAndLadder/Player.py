class Player:
    def __init__(self, id: str, current_position: int = 0):
        self.id = id
        self.current_position = current_position

    def __repr__(self):
        return f"Player(id={self.id!r}, pos={self.current_position})"
