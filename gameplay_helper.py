import piece as Piece
import rank as Rank
import main
import json
import square as Square
from typing import List
import pygame
import numpy as np
import gameplay
import helpers

def dictionary_to_object(data_dict: dict):  
    """Turns dictionaries into objects

    Args:
        data_dict (dict): A dictionary containing the properties of a square as keys and values (e.g. 'name': 'a6' ).

    Returns:
        square (Square): Info about a particular square on the board
    """
    square = Square.Square(data_dict["top_left_x"], data_dict["top_left_y"], data_dict["bottom_right_x"], data_dict["bottom_right_y"], data_dict["name"], data_dict["piece_occupying"])

    return square 

#stuff that was in helpers
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
    clicked_square_name = helpers.find_clicked_square((selected_sprite.x, selected_sprite.y), helpers.get_squares())
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

def update_squares_from_json() ->list[Square.Square]: 
    """Adds info about each square from the json file to square

    Returns:
        squares (list): List of square
    """
    squares = []

    f = open('squareInfo.json')
    data_dictionary = json.load(f)
    f.close()

    for square in data_dictionary["squares"]:
        squares.append(helpers.dictionary_to_object(square))    

    return squares

def highlight_squares(valid_moves: List[str]): 
    """Draws rectangles to highlight the squares that are part of the valid_moves for selected_piece.

    Args:
        squares (List[Square.Square]): A list of all squares
    """
    squares_to_highlight = []
    squares = update_squares_from_json()


    for valid_move in valid_moves:
        for square in squares:
            if square.name[0] == valid_move[0] and square.name[1] == valid_move[1]:
                squares_to_highlight.append(square)

    for square in squares_to_highlight:
        width = np.abs(square.bottom_right_x - square.top_left_x)
        height = np.abs(square.bottom_right_y - square.top_left_y)

        pygame.draw.rect(gameplay.screen, (54, 152, 200, 0), (square.top_left_x, square.top_left_y, width, height))

    pygame.display.flip()

    return