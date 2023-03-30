import unittest
import piece as Piece
import square as Square
import rank as Rank
import ui




class find_clicked_square(unittest.TestCase):    
    def test_find_clicked_square1(self):
        coordinates = (385, 116)
        squares = ui.initialize_squares()
        
        result = ui.find_clicked_square(coordinates, squares)

        self.assertEqual(result, "f7")    
        
    def test_find_clicked_square2(self):
        coordinates = (529, 309)
        squares = ui.initialize_squares()
        
        result = ui.find_clicked_square(coordinates, squares)

        self.assertEqual(result, "h4")
        
    def test_find_clicked_square3(self):
        coordinates = (176, 390)
        squares = ui.initialize_squares()
        
        result = ui.find_clicked_square(coordinates, squares)

        self.assertEqual(result, "c3")

class movement_of_selected_piece(unittest.TestCase):
    def test_pawn_movement1(self):
        selected_piece = Piece.Piece("white", "c", 2, Rank.Rank(1), 0)

        result = ui.get_movement_of_selected_piece(selected_piece)
        expected = ["c3", "c4"]

        self.assertEqual(len(expected), len(result))
        self.assertSequenceEqual(sorted(expected), sorted(result))


    def test_pawn_movement2(self):
        selected_piece = Piece.Piece("black", "c", 6, Rank.Rank(1), 1)

        result = ui.get_movement_of_selected_piece(selected_piece)
        expected = ["c5"]
          
        self.assertEqual(len(expected), len(result))
        self.assertSequenceEqual(sorted(expected), sorted(result))
  

    def test_knight_movement1(self):
        selected_piece = Piece.Piece("black", "g", 8, Rank.Rank(2), 0)

        result = ui.get_movement_of_selected_piece(selected_piece)
        expected = ["f6", "h6"]

        self.assertEqual(len(expected), len(result))
        self.assertSequenceEqual(sorted(expected), sorted(result))


    def test_knight_movement2(self):
        selected_piece = Piece.Piece("white", "b", 1, Rank.Rank(2), 1)

        result = ui.get_movement_of_selected_piece(selected_piece)
        expected = ["a3", "c3"]

        self.assertEqual(len(expected), len(result))
        self.assertSequenceEqual(sorted(expected), sorted(result))


class dict_to_object(unittest.TestCase):
    def test1(self):
        data_dict = {"top_left_x" : 284, "top_left_y" : 9, "bottom_right_x" : 350, "bottom_right_y" : 76, "name" : "e8",
                        "piece_occupying" : "king"  }
        
        result = ui.dictionary_to_object(data_dict)
        expected = Square.Square(284, 9, 350, 76, "e8", "king")

        self.assertEqual(result.bottom_right_x, expected.bottom_right_x)    
        self.assertEqual(result.bottom_right_y, expected.bottom_right_y)    
        self.assertEqual(result.name, expected.name)    
        self.assertEqual(result.top_left_x, expected.top_left_x)    
        self.assertEqual(result.top_left_y, expected.top_left_y)    
        self.assertEqual(result.piece_occupying, expected.piece_occupying)    




if __name__ == '__main__':
    unittest.main()