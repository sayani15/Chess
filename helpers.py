import piece as Piece
import rank as Rank
import main
import json
import square as Square
from typing import List
import pygame
import numpy as np
from enum import Enum
import clickable_sprite as ClickableSprite

    


def get_valid_moves_for_piece_object(selected_piece: Piece.Piece) -> list[str]: 
    
    """Finds the rank of the player's selected sprite and returns the valid moves for it in its current position.

    Args:
        selected_sprite (pygame.sprite): The sprite that has been selected by the player.

    Raises:
        Exception: Raises exception if selected_sprite's rank does not match a valid rank.

    Returns:
        valid_moves (list) : List of available moves for the sprite piece.
    """
    movement_functions = {
        Rank.Rank.pawn.value: main.pawn_movement,
        Rank.Rank.knight.value: main.knight_movement,
        Rank.Rank.bishop.value: main.bishop_movement,
        Rank.Rank.rook.value: main.rook_movement,
        Rank.Rank.queen.value: main.queen_movement,
        Rank.Rank.king.value: main.king_movement,
    }

    if selected_piece.rank not in movement_functions:
        raise Exception

    pieces_in_play = get_pieces_in_play_from_json()
    piece = Piece.Piece(selected_piece.colour, selected_piece.x_position, int(selected_piece.y_position), selected_piece.rank, selected_piece.move_counter)

    valid_moves = movement_functions[selected_piece.rank](pieces_in_play, piece)
  
    return valid_moves

def get_valid_moves(selected_sprite: ClickableSprite.ClickableSprite) -> list[str]: 
    """Finds the rank of the player's selected sprite and returns the valid moves for it in its current position.

    Args:
        selected_sprite (pygame.sprite): The sprite that has been selected by the player.

    Raises:
        Exception: Raises exception if selected_sprite's rank does not match a valid rank.

    Returns:
        valid_moves (list) : List of available moves for the sprite piece.
    """
    movement_functions = {
        Rank.Rank.pawn.value: main.pawn_movement,
        Rank.Rank.knight.value: main.knight_movement,
        Rank.Rank.bishop.value: main.bishop_movement,
        Rank.Rank.rook.value: main.rook_movement,
        Rank.Rank.queen.value: main.queen_movement,
        Rank.Rank.king.value: main.king_movement,
    }

    if selected_sprite.rank not in movement_functions:
        raise Exception

    if selected_sprite is not None:
        pieces_in_play = get_pieces_in_play_from_json()
        clicked_square_name = find_clicked_square((selected_sprite.rect.centerx, selected_sprite.rect.centery), get_squares())
        piece = Piece.Piece(selected_sprite.colour, clicked_square_name[0], int(clicked_square_name[1]), selected_sprite.rank, selected_sprite.move_counter)

        valid_moves = movement_functions[selected_sprite.rank](pieces_in_play, piece)
        return valid_moves
    else:
        raise Exception

    

def find_clicked_square(coordinates: tuple, squares: List[Square.Square]) -> str: 
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

def get_rank_from_string_piece_occupying(piece_occupying) -> Rank:
    """Converts the name of the piece as a string, e.g. "knight" to a Rank.Rank()

    Args:
        piece_occupying (str): The type of piece. E.g "rook"

    Returns:
        rank (Rank): The rank of the piece. E.g. name: 'rook', value: 4
    """
    if piece_occupying == "pawn":
        rank = Rank.Rank(1)
    if piece_occupying == "knight":
        rank = Rank.Rank(2)
    if piece_occupying == "bishop":
        rank = Rank.Rank(3)
    if piece_occupying == "rook":
        rank = Rank.Rank(4)
    if piece_occupying == "queen":
        rank = Rank.Rank(5)
    if piece_occupying == "king":
        rank = Rank.Rank(6)

    return rank
    

def get_squares() -> list[Square.Square]:
    """Gets a list of square objects from squareInfo.json

    Returns:
        list[Square.Square]: A list of squares
    """
    with open('squareInfo.json', 'r') as file:
        data_dictionary = json.load(file)

    squares = []

    for square in data_dictionary["squares"]:
        squares.append(dictionary_to_square_object(square))

    return squares

def get_pieces_in_play_from_json() -> list[Piece.Piece]:
    """Gets a list of piece objects from pieceInfo.json and squareInfo.json

    Returns:
        list[Piece.Piece]: A list of pieces
    """
    pieces = []

    with open('squareInfo.json', 'r') as file:
        square_data_dict = json.load(file)

    with open('pieceInfo.json', 'r') as file:
        piece_data_dict = json.load(file)

    for square in square_data_dict["squares"]:
        for piece in piece_data_dict["pieces"]:
            if square["name"] == piece["name"]:
                pieces.append(dictionary_to_piece_object(piece, square))

    return pieces
    

def update_squareInfojson(previous_square_name: str, moved_piece_rank: str, square_name: str):
    """Updates "piece_occupying" part of squareInfo.json

    Args:
        previous_square_name (str): The name of the square the piece was on in the previous move
        moved_piece_rank (str): Rank of the piece that's been moved
        square_name (str): The name of the square that the piece has been moved to.
    """
    
    try:
        with open('squareInfo.json', 'r') as f:
            data = json.load(f)

        # Remove piece from previous square
        for d in data["squares"]:
            if previous_square_name == d["name"]:
                d["piece_occupying"] = ""
                break        
            
        # Place piece in new square    
        for d in data["squares"]:
            if square_name == d["name"]:
                if d["piece_occupying"] != "":
                    print(f"Piece in {square_name} has been taken.")
                d["piece_occupying"] = str(moved_piece_rank)
                break
        

        with open('squareInfo.json', 'w') as f:
            json.dump(data, f, indent = 4)


    except Exception as e:
        print("Error: Unable to parse JSON data from file.")
        print("Details:", e)

def update_pieceInfojson(previous_square_name: str, square_name: str, is_take_piece_action: bool = False):
    """Updates "name" part of pieceInfo.json

    Args:
        previous_piece_name (str): The name of the square the piece was on in the previous move
        square_name (str): The name of the square that the piece has been moved to.
    """
    
    try:
        with open('pieceInfo.json', 'r') as f:
            data = json.load(f)

        # Change name of square piece is in
        if is_take_piece_action == False:
            for d in data["pieces"]:
                if previous_square_name == d["name"]:
                    d["name"] = str(square_name)
                    break        
        
        # Remove piece from previous square
        if is_take_piece_action:
            for d in data["pieces"]:
                if square_name == d["name"]:
                    d["name"] = ""
                    d["colour"] = ""
                    d["move_counter"] = 0
                if previous_square_name == d["name"]:
                    d["name"] = str(square_name)
                      
            

        with open('pieceInfo.json', 'w') as f:
            json.dump(data, f, indent = 4)


    except Exception as e:
        print("Error: Unable to parse JSON data from file.")
        print("Details:", e)


def dictionary_to_square_object(data_dict: dict) -> Square.Square:  
    """Turns dictionaries into objects

    Args:
        data_dict (dict): A dictionary containing the properties of a square as keys and values (e.g. 'name': 'a6' ).

    Returns:
        square (Square): Info about a particular square on the board
    """
    square = Square.Square(data_dict["top_left_x"], data_dict["top_left_y"], data_dict["bottom_right_x"], data_dict["bottom_right_y"], data_dict["name"], data_dict["piece_occupying"])

    return square 

def dictionary_to_piece_object(piece_data_dict: dict, square_data_dict: dict) -> Piece.Piece:  
    """Turns dictionaries into objects.

    Args:
        piece_data_dict (dict): A dictionary containing info about the properties of a piece using the data in 
                                pieceInfo.json) as keys and values (e.g. 'name': 'a6', or 'colour': 'black').
        square_data_dict (dict): A dictionary containing the properties of a square as keys and values (e.g. 'name': 'a6' ).

    Returns:
        piece (Piece): Info about a particular piece on the board
    """
    rank = square_data_dict["piece_occupying"]
    
    piece = Piece.Piece(piece_data_dict["colour"], piece_data_dict["name"][0], int(piece_data_dict["name"][1]), 
                        rank, piece_data_dict["move_counter"])

    return piece 


def update_squares_from_json() -> list[Square.Square]: 
    """Adds info about each square from the json file to square

    Returns:
        squares (list): List of square
    """
    squares = []

    with open('squareInfo.json', 'r') as file:
        data_dictionary = json.load(file)

    for square in data_dictionary["squares"]:
        squares.append(dictionary_to_square_object(square))    

    return squares
# is this method needed? its the same as get_squares()

def revert_json_changes():
    """Uses piece and square InfoInitial json files to send all pieces and squares back to their original states in piece/squareInfo
       when the program is closed.
    """
    try:
        with open('pieceInfoInitial.json', 'r') as f:
            data = json.load(f)

        with open('pieceInfo.json', 'w') as f:
            json.dump(data, f, indent = 4)

    except Exception as e:
        print("Error: Unable to parse JSON data from file.")
        print("Details:", e)


    try:
        with open('squareInfoInitial.json', 'r') as f:
            data = json.load(f)

        with open('squareInfo.json', 'w') as f:
            json.dump(data, f, indent = 4)

    except Exception as e:
        print("Error: Unable to parse JSON data from file.")
        print("Details:", e)

    return


    
     

