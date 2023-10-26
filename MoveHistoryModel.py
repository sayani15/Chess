import piece as Piece

class MoveHistoryModel:
    def __init__(self, from_square: str, to_square: str, piece: Piece):
        self.from_square = from_square
        self.to_square = to_square
        self.piece = piece
