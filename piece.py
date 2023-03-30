import rank as Rank

class Piece:
    def __init__(self, colour: str, x_position: str, y_position: int, rank: Rank.Rank, move_counter: int):
        self.colour = colour
        self.x_position = x_position
        self.y_position = y_position
        self.rank = rank
        self.move_counter = move_counter

