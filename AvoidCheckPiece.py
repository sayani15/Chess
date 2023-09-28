import piece as Piece

class AvoidCheckPiece:
    def __init__(self, piece: Piece.Piece, valid_moves: list[str]):
        self.piece = piece
        self.valid_moves = valid_moves
      