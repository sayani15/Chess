import unittest
import check_helper
import piece as Piece
import rank as Rank
import clickable_sprite as ClickableSprite
from unittest.mock import MagicMock

class FindPiecesToBlockTestCases(unittest.TestCase):
    #pawn as piece_checking_king
    def test_pawn_checking_king_0_blocks_possible(self):
        pieces_in_play = []
        
        king_in_check = Piece.Piece("white", "e", 1, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("black", "f", 2, Rank.Rank(1), 0)

        result = check_helper.find_pieces_to_block_check(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = []
        
        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    #knight as piece_checking_king
    def test_knight_checking_king_0_blocks_possible(self):
        pieces_in_play = []
        
        king_in_check = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "d", 6, Rank.Rank(4), 0)

        result = check_helper.find_pieces_to_block_check(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = []
        
        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))
    
    #rook as piece_checking_king
    def test_rook_checking_king_0_blocks_possible(self):
        pieces_in_play = []
        
        king_in_check = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "h", 8, Rank.Rank(4), 0)

        result = check_helper.find_pieces_to_block_check(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = []
        
        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    def test_rook_checking_king_2_blocks_possible(self):
        pieces_in_play = []
        pieces_in_play.append(Piece.Piece("black", "g", 4, Rank.Rank(4), 0))
        pieces_in_play.append(Piece.Piece("black", "f", 7, Rank.Rank(4), 0))
        
        king_in_check = Piece.Piece("black", "a", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "h", 8, Rank.Rank(4), 0)

        result = check_helper.find_pieces_to_block_check(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = [Piece.Piece("black", "g", 4, Rank.Rank(4), 0), Piece.Piece("black", "f", 7, Rank.Rank(4), 0)]
        
        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

    #bishop as piece_checking_king
    def test_bishop_checking_king_0_blocks_possible(self):
        pieces_in_play = []
        
        king_in_check = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "f", 7, Rank.Rank(4), 0)

        result = check_helper.find_pieces_to_block_check(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = []
        
        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))
    
    #queen as piece_checking_king
    def test_queen_checking_king_0_blocks_possible(self):
        pieces_in_play = []
        
        king_in_check = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "h", 8, Rank.Rank(4), 0)

        result = check_helper.find_pieces_to_block_check(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = []
        
        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))

class FindPiecesToTakeTestCases(unittest.TestCase):
    def test_0_ways_to_take(self):
        pieces_in_play = []
        
        king_in_check = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "h", 8, Rank.Rank(4), 0)

        result = check_helper.find_pieces_to_take_checking_piece(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = []

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result)) 

    def test_1_way_to_take(self):
        king_in_check = Piece.Piece("black", "e", 8, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "h", 8, Rank.Rank(4), 0)

        pieces_in_play = []
        pieces_in_play.append(Piece.Piece("black", "h", 6, Rank.Rank(2), 0))
        pieces_in_play.append(king_in_check)
        pieces_in_play.append(piece_checking_king)

        result = check_helper.find_pieces_to_take_checking_piece(king_in_check, piece_checking_king, pieces_in_play)
        expected_result = [Piece.Piece("black", "h", 6, Rank.Rank(2), 0)]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))
    
    def test_every_rank_of_piece_to_take_with(self):
        pieces_in_play = []
        pieces_in_play.append(Piece.Piece("black", "g", 5, Rank.Rank(5), 0))
        pieces_in_play.append(Piece.Piece("black", "e", 5, Rank.Rank(4), 0))
        pieces_in_play.append(Piece.Piece("black", "f", 2, Rank.Rank(3), 0))
        pieces_in_play.append(Piece.Piece("black", "g", 4, Rank.Rank(2), 0))
        pieces_in_play.append(Piece.Piece("black", "d", 1, Rank.Rank(1), 0))

        king_in_check = Piece.Piece("black", "c", 1, Rank.Rank(6), 0)
        piece_checking_king = Piece.Piece("white", "e", 3, Rank.Rank(5), 0)

        result = check_helper.find_pieces_to_take_checking_piece(king_in_check, piece_checking_king, pieces_in_play)
        expected_result =  [Piece.Piece("black", "g", 5, Rank.Rank(5), 0),
                            Piece.Piece("black", "e", 5, Rank.Rank(4), 0),
                            Piece.Piece("black", "f", 2, Rank.Rank(3), 0),
                            Piece.Piece("black", "g", 4, Rank.Rank(2), 0),
                            Piece.Piece("black", "d", 1, Rank.Rank(1), 0)]

        self.assertEqual(len(expected_result), len(result))
        self.assertSequenceEqual(sorted(expected_result), sorted(result))
    


if __name__ == '__main__':
    unittest.main()