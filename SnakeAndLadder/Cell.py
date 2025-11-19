from typing import Optional
from Jump import Jump
class Cell:
    def __init__(self):
        self.jump: Optional[Jump] = None

    def __repr__(self):
        return f"Cell(jump={self.jump})"

