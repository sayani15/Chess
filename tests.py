import unittest
import piece as Piece
import rank as Rank
import main


class IsSquareOccupiedTestCases(unittest.TestCase):
    def test_square_is_occupied(self):
        pieces = []
        pieces.append(Piece.Piece("black", "d", 2, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "a", 8, Rank.Rank(4), 0))
        pieces.append(Piece.Piece("black", "e", 8, Rank.Rank(3), 0))
        pieces.append(Piece.Piece("black", "d", 7, Rank.Rank(5), 0))

        result = main.is_square_occupied(pieces, "a", 8)

        self.assertEqual(result, True)

    def test_square_is_not_occupied(self):
        pieces = []
        pieces.append(Piece.Piece("black", "d", 2, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "a", 8, Rank.Rank(4), 0))
        pieces.append(Piece.Piece("black", "e", 8, Rank.Rank(3), 0))
        pieces.append(Piece.Piece("black", "d", 7, Rank.Rank(5), 0))

        result = main.is_square_occupied(pieces, "a", 5)

        self.assertEqual(result, False)


class GetPawnMovementTestCases(unittest.TestCase):
    def test_no_moves_available_black(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "d", 6, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, [])

    def test_no_moves_available_black2(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("white", "d", 6, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "d", 5, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, [])

    def test_no_moves_available_white(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "d", 3, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, [])

    def test_no_moves_available_white2(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("white", "d", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("black", "d", 4, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, [])

    def test_one_space_move_available_white(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "d", 4, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, ["d3"])

    def test_one_space_move_available_black(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "d", 5, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, ["d6"])

    def test_two_spaces_move_available_white(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "d", 5, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["d3", "d4"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_two_spaces_move_available_black(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "d", 4, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["d6", "d5"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_take_diagonal_piece_move_available_black_taking_black_fails(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "e", 6, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("black", "c", 6, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["d5", "d6"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_take_diagonal_piece_move_available_white_taking_white_fails(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("white", "e", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "c", 3, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["d3", "d4"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_take_diagonal_piece_move_available_white_taking_black_passes(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "e", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("black", "c", 3, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["c3", "e3", "d3", "d4"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_take_diagonal_piece_move_available_black_taking_white_passes(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("white", "e", 6, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "c", 6, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["c6", "e6", "d6", "d5"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_only_take_diagonal_piece_move_available_black_taking_white(self):
        piece = Piece.Piece("black", "d", 7, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("white", "e", 6, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "d", 6, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "c", 6, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["c6", "e6"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_only_take_diagonal_piece_move_available_white_taking_black(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 0)
        pieces = []
        pieces.append(Piece.Piece("black", "e", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "d", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("black", "c", 3, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["c3", "e3"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_pawn_can_only_move_one_space_if_not_first_move(self):
        piece = Piece.Piece("white", "d", 2, Rank.Rank(1), 1)
        pieces = []
        pieces.append(Piece.Piece("black", "e", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "d", 5, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("black", "c", 3, Rank.Rank(5), 0))

        result = main.pawn_movement(pieces, piece)
        expected_result = ["c3", "e3", "d3"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))


class GetRookMovementTestCases(unittest.TestCase):
    def test_move_upwards_in_empty_board_black(self):
        piece = Piece.Piece("black", "d", 4, Rank.Rank(4), 0)

        result = main.rook_movement([], piece)

        self.assertEqual(sorted(["d5", "d6", "d7", "d8"]), sorted(result))

    def test_move_upwards_with_upwards_black_blocked_by_black(self):
        piece = Piece.Piece("black", "d", 4, Rank.Rank(4), 0)

        pieces = []
        pieces.append(Piece.Piece("black", "d", 7, Rank.Rank(4), 0))
        result = main.rook_movement(pieces, piece)

        self.assertEqual(sorted(["d5", "d6"]), sorted(result))

    def test_move_upwards_with_upwards_white_in_path_of_black(self):
        piece = Piece.Piece("black", "d", 4, Rank.Rank(4), 0)

        pieces = []
        pieces.append(Piece.Piece("white", "d", 7, Rank.Rank(4), 0))
        result = main.rook_movement(pieces, piece)

        self.assertEqual(sorted(["d5", "d6", "d7"]), sorted(result))


if __name__ == '__main__':
    unittest.main()
