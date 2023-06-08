import piece as Piece
import rank as Rank
import main
import gameplay
import json
import square as Square

def find_clicked_square(coordinates: tuple, squares: List[Square.Square] ): 
    """Finds the name of the square when given coordinates of position.

    Args:
        coordinates (tuple): Tuple containing coordinates of position that has been clicked on 
        squares (List[Square.Square]): List of squares

    Returns:
        square.name (string): Name of square
    """
    #TODO: If user clicks outside grid 
    for square in squares:
        if coordinates[0] > square.top_left_x and coordinates[0] < square.bottom_right_x and \
         coordinates[1] > square.top_left_y and coordinates[1] < square.bottom_right_y:
            return square.name

def get_squares():
    f = open('squareInfo.json')
    data_dictionary = json.load(f)
    f.close()
    squares = []

    for square in data_dictionary["squares"]:
            squares.append(dictionary_to_object(square))

    return squares

def dictionary_to_object(data_dict: dict):  
    """Turns dictionaries into objects

    Args:
        data_dict (dict): A dictionary containing the properties of a square as keys and values (e.g. 'name': 'a6' ).

    Returns:
        square (Square): Info about a particular square on the board
    """
    square = Square.Square(data_dict["top_left_x"], data_dict["top_left_y"], data_dict["bottom_right_x"], data_dict["bottom_right_y"], data_dict["name"], data_dict["piece_occupying"])

    return square 

def get_valid_moves(selected_sprite: gameplay.ClickableSprite): 
    """Finds the rank of the player's selected piece and returns the valid moves for the piece in its current position.

    Args:
        selected_piece (Piece): The piece that has been selected by the player.

    Raises:
        Exception: Raises exception if selected_piece's rank does not match a valid rank.

    Returns:
        valid_moves (list) : List of available moves for the piece.
    """
    pieces_in_play = main.create_pieces()
    clicked_square_name = find_clicked_square((selected_sprite.x, selected_sprite.y), get_squares())
    piece = Piece(selected_sprite.colour, clicked_square_name[0], clicked_square_name[1], selected_sprite.rank, selected_sprite.move_counter)

    if selected_sprite.rank == Rank.Rank.pawn:
        valid_moves = main.pawn_movement(pieces_in_play, piece)
    elif selected_sprite.rank == Rank.Rank.knight:
        valid_moves = main.knight_movement(pieces_in_play, piece)
    elif selected_sprite.rank == Rank.Rank.bishop:
        valid_moves = main.bishop_movement(pieces_in_play, piece)
    elif selected_sprite.rank == Rank.Rank.rook:
        valid_moves = main.rook_movement(pieces_in_play, piece)
    elif selected_sprite.rank == Rank.Rank.queen:
        valid_moves = main.queen_movement(pieces_in_play, piece)
    elif selected_sprite.rank == Rank.Rank.king:
        valid_moves = main.king_movement(pieces_in_play, piece)  
    else:
        raise Exception     
    
    return valid_moves