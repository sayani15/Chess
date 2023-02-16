class Square:
    def __init__(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y, name, piece_occupying):
        """

        Args:
            top_left_x (int): x coordinate of top left of square
            top_left_y (int): y coordinate of top left of square
            bottom_right_x (int): x coordinate of bottom right of square
            bottom_right_y (int): y coordinate of bottom right of square

            name (string): Name of square
            piece_occupying (piece): If there's a piece occupying the square, and information about the piece.
        """
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.bottom_right_x = bottom_right_x
        self.bottom_right_y = bottom_right_y

        self.name = name
        self.piece_occupying = piece_occupying

