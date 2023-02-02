from enum import Enum


class Rank(Enum):
    pawn = 1    # (1 material point)
    knight = 2    # (3 material points)
    bishop = 3    # (3 material points)
    rook = 4    # (5 material points)
    queen = 5    # (9 material points)
    king = 6    # (no assigned value)
