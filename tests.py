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

    def test_move_up_while_in_row_8(self):  # doesnt know not to go off board
        piece = Piece.Piece("white", "d", 8, Rank.Rank(1), 0)
        pieces = []

        result = main.pawn_movement(pieces, piece)

        self.assertEqual(result, [])

    def test_move_down_while_in_row_1(self):  # doesnt know not to go off board
        piece = Piece.Piece("black", "d", 1, Rank.Rank(1), 0)
        pieces = []

        result = main.pawn_movement(pieces, piece)

        self.assertEqual([], result)


class GetBishopMovementTestCases(unittest.TestCase):
    def test_move_in_empty_board(self):
        piece = Piece.Piece("white", "e", 4, Rank.Rank(3), 0)

        pieces = []
        result = main.bishop_movement(pieces, piece)
        expected_result = ["d3", "c2", "b1", "f5", "g6", "h7", "d5", "c6", "b7", "a8", "f3", "g2", "h1"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_one_move_available(self):
        piece = Piece.Piece("white", "e", 4, Rank.Rank(3), 0)

        pieces = []
        pieces.append(Piece.Piece("white", "d", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "d", 5, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "f", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("black", "f", 5, Rank.Rank(5), 0))

        result = main.bishop_movement(pieces, piece)
        expected_result = ["f5"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_one_direction_available(self):
        piece = Piece.Piece("white", "e", 4, Rank.Rank(3), 0)

        pieces = []
        pieces.append(Piece.Piece("white", "d", 5, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "f", 3, Rank.Rank(5), 0))
        pieces.append(Piece.Piece("white", "f", 5, Rank.Rank(5), 0))

        result = main.bishop_movement(pieces, piece)
        expected_result = ["d3", "c2", "b1"]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))


#class GetKnightMovementTestCases(unittest.TestCase):


class GetRookMovementTestCases(unittest.TestCase):
    def test_move_in_empty_board(self):
        piece = Piece.Piece("white", "d", 4, Rank.Rank(4), 0)

        result = main.rook_movement([], piece)

        self.assertEqual(sorted(["a4", "b4", "c4", "d1", "d2", "d3", "d5", "d6", "d7", "d8", "e4", "f4", "g4", "h4"]), sorted(result))

    def test_move_with_upwards_black_blocked_by_black(self):
        piece = Piece.Piece("black", "d", 4, Rank.Rank(4), 0)

        pieces = []
        pieces.append(Piece.Piece("black", "d", 7, Rank.Rank(4), 0))
        result = main.rook_movement(pieces, piece)

        self.assertEqual(sorted(["a4", "b4", "c4", "d1", "d2", "d3", "d5", "d6", "e4", "f4", "g4", "h4"]), sorted(result))

    def test_move_with_upwards_white_in_path_of_black(self):
        piece = Piece.Piece("black", "d", 4, Rank.Rank(4), 0)

        pieces = []
        pieces.append(Piece.Piece("white", "d", 7, Rank.Rank(4), 0))
        result = main.rook_movement(pieces, piece)

        self.assertEqual(sorted(["a4", "b4", "c4", "d1", "d2", "d3", "d5", "d6", "d7", "e4", "f4", "g4", "h4"]), sorted(result))


class GetQueenMovementTestCases(unittest.TestCase):
    # def test_move_in_empty_board_from_middle(self):
    #     piece = Piece.Piece("white", "e", 4, Rank.Rank(6), 0)

    #     result = main.queen_movement([], piece)

    #     self.assertEqual(sorted([ "e1", "e2", "e3", "e5", "e6", "e7", "e8",
    #                               "a4", "b4", "c4", "d4", "f4", "g4", "h4",
    #                               "b8", "c7", "d6", "" "f4", "d5"
    #                               "f3", "d3", ]), sorted(result))

    def test_1_move_available(self):
        piece = Piece.Piece("black", "d", 5, Rank.Rank(6), 0)

        pieces = []
        pieces.append(Piece.Piece("black", "d", 6, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "d", 4, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "e", 5, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "c", 5, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "e", 4, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "c", 4, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "e", 6, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "b", 7, Rank.Rank(6), 0))
        

        result = main.queen_movement(pieces, piece)

        self.assertEqual(sorted(["c6"]), sorted(result))


class GetKingMovementTestCases(unittest.TestCase):
    def test_move_in_empty_board_from_middle_white(self):
        piece = Piece.Piece("white", "e", 4, Rank.Rank(6), 0)

        result = main.king_movement([], piece)

        self.assertEqual(sorted(["e5", "e3", "d4", "f4", "f3", "d3", "f5", "d5"]), sorted(result))

    def test_move_in_empty_board_from_middle_black(self):
        piece = Piece.Piece("black", "e", 4, Rank.Rank(6), 0)

        result = main.king_movement([], piece)

        self.assertEqual(sorted(["e5", "e3", "d4", "f4", "f3", "d3", "f5", "d5"]), sorted(result))

    def test_move_in_empty_board_from_1(self):
        piece = Piece.Piece("white", "e", 1, Rank.Rank(6), 0)

        result = main.king_movement([], piece)

        self.assertEqual(sorted(["e2", "d2", "f2", "d1", "f1"]), sorted(result))

    def test_move_in_empty_board_from_8(self):
            piece = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)

            result = main.king_movement([], piece)

            self.assertEqual(sorted(["e7", "d7", "f7", "d8", "f8"]), sorted(result))

    def test_move_in_empty_board_from_a(self):
        piece = Piece.Piece("black", "a", 4, Rank.Rank(6), 0)

        result = main.king_movement([], piece)

        self.assertEqual(sorted(["a5", "a3", "b3", "b4", "b5"]), sorted(result))

    def test_move_in_empty_board_from_h(self):
        piece = Piece.Piece("black", "a", 5, Rank.Rank(6), 0)

        result = main.king_movement([], piece)

        self.assertEqual(sorted(["a4", "a6", "b4", "b5", "b6"]), sorted(result))

    def test_1_move_available(self):
        piece = Piece.Piece("black", "d", 5, Rank.Rank(6), 0)

        pieces = []
        pieces.append(Piece.Piece("black", "d", 6, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "d", 4, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "e", 5, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "c", 5, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "e", 4, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "c", 4, Rank.Rank(6), 0))
        pieces.append(Piece.Piece("black", "e", 6, Rank.Rank(6), 0))
        result = main.king_movement(pieces, piece)

        self.assertEqual(sorted(["c6"]), sorted(result))



if __name__ == '__main__':
    unittest.main()
