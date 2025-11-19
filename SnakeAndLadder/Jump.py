class Jump:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        typ = "ladder" if self.end > self.start else "snake"
        return f"{typ}({self.start} -> {self.end})"

