import rank as Rank

class Piece_pixel_positions:
    def __init__(self, colour: str, x_pixel_position: int, y_pixel_position: int, rank: Rank.Rank):
        self.colour = colour
        self.x_pixel_position = x_pixel_position
        self.y_pixel_position = y_pixel_position
        self.rank = rank

