import piece as Piece
import rank as Rank
import AvoidCheckPiece as AvoidCheckPiece
import clickable_sprite as ClickableSprite
from typing import List
import helpers
import main
import numpy as np


def is_in_check(king_to_be_checked_position: str, colour_to_be_checked: str, sprites_in_play: list[ClickableSprite.ClickableSprite]):
    """Checks if the king is in check or not.

    Args:
        king_to_be_checked_position (str): The position of the king that is being threatened by a check.
        colour_to_be_checked (str): The colour of the king to be checked.
        sprites_in_play (list[ClickableSprite.ClickableSprite]): A list of all the ClickableSprites currently on the board.

    Returns:
        bool: True if the king is in check, false if not.
    """
    valid_moves = []

    for sprite in sprites_in_play:
        if sprite.colour != colour_to_be_checked:
            sprite_valid_moves = helpers.get_valid_moves(sprite)
            for move in sprite_valid_moves:
                valid_moves.append(move)
    for valid_move in valid_moves:
        if valid_move == king_to_be_checked_position:
            print("in check")
            return True
    print("not in check")
    return False

def find_pieces_to_take_checking_piece(piece_checking_king: Piece.Piece, pieces_in_play: list[Piece.Piece]):
    """Finds pieces that can take the checking piece

    Args:
        piece_checking_king (Piece.Piece): _description_
        pieces_in_play (list[Piece.Piece]): _description_

    Returns:
        result (list[AvoidCheckPiece]): (piece that can take, valid_move - which will be the position of the checking piece (probably?))
    """
    result = []
    
    for piece in pieces_in_play:
        if piece.colour != piece_checking_king.colour:
            piece_valid_moves = helpers.get_valid_moves_for_piece_object(piece, pieces_in_play)
            for valid_move in piece_valid_moves:
                if valid_move == f"{piece_checking_king.x_position}{piece_checking_king.y_position}":
                    result.append(AvoidCheckPiece.AvoidCheckPiece(piece, [valid_move]))   #TODO: Verify that there will only ever be one valid move
                    
    return result 

def find_pieces_to_block_check(king_in_check: Piece.Piece, piece_checking_king: Piece.Piece, pieces_in_play: list[Piece.Piece]): 
    """Finds pieces from the checked side to take the checking piece.

    Args:
        king_in_check (Piece.Piece): King being checked
        piece_checking_king (Piece.Piece): The piece on the checking side attacking the king.
        pieces_in_play (list[Piece.Piece]): A list of all the pieces currently on the board.

    Returns:
        result (list[AvoidCheckPiece]): A list of AvoidCheckPiece (piece to block, list of moves it can go to to block)
    """
    all_valid_moves = {}
    
    for piece in pieces_in_play:
        if piece.colour != piece_checking_king.colour and piece.rank != king_in_check.rank:
            piece_valid_moves = helpers.get_valid_moves_for_piece_object(piece, pieces_in_play) # list of valid moves for piece
            all_valid_moves.update({piece : piece_valid_moves})
            

    if piece_checking_king.rank == Rank.Rank.knight.name or piece_checking_king == Rank.Rank.pawn.name:
        print("impossible to block sorry")
        return None
    else:
        #PIECE CHECKING KING
        pieces_to_enable_blocking = []
        king_in_check_x, piece_checking_king_x = main.converts_letter_to_number(king_in_check.x_position),  main.converts_letter_to_number(piece_checking_king.x_position)
        squares_to_king_x = king_in_check_x - piece_checking_king_x 
        squares_to_king_y = king_in_check.y_position - piece_checking_king.y_position 
        squares_to_block_check = []

        if squares_to_king_y < squares_to_king_x:
            for i in np.arange(1, squares_to_king_x):
                squares_to_block_check.append(f"{main.examine_x_positions(piece_checking_king.x_position, i)}{piece_checking_king.y_position}")
        elif squares_to_king_y > squares_to_king_x:  
            for i in range(1, squares_to_king_y):
                squares_to_block_check.append(f"{piece_checking_king.x_position}{piece_checking_king.y_position + i}")
        else:
            for i in range(1, squares_to_king_y):
                squares_to_block_check.append(f"{main.examine_x_positions(piece_checking_king.x_position, i)}{piece_checking_king.y_position + i}")



        if squares_to_king_y < squares_to_king_x:
            for i in range(1, squares_to_king_x):
                square = f"{main.examine_x_positions(piece_checking_king.x_position, i)}{piece_checking_king.y_position}"
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                        if vm == square:
                            pieces_to_enable_blocking.append(piece)
        elif squares_to_king_y > squares_to_king_x:
            for i in range(1, squares_to_king_y):
                square = f"{piece_checking_king.x_position}{piece_checking_king.y_position + i}"
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                        if vm == square:
                            pieces_to_enable_blocking.append(piece)
        else:
            for i in range(1, squares_to_king_x):
                square = f"{main.examine_x_positions(piece_checking_king.x_position, i)}{piece_checking_king.y_position+i}"
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                        if vm == square:
                            pieces_to_enable_blocking.append(piece)         
    

    partial_result = []     # list[AvoidCheckPiece]: contains all the pieces that can block the check, 
                            # but the valid_moves of each piece are not filtered yet to only include moves that will block the check
    for piece in pieces_to_enable_blocking:
        partial_result.append(AvoidCheckPiece.AvoidCheckPiece(piece, all_valid_moves[piece]))

    result = []

    #filters the relevant valid moves from the useless ones
    for r in partial_result:
        relevant_vms = []
        for valid_move in r.valid_moves:
            if valid_move in squares_to_block_check:   
                relevant_vms.append(valid_move)
        result.append(AvoidCheckPiece.AvoidCheckPiece(r.piece, relevant_vms)) 
               
    return result   

def run_to_avoid_checkmate(king_in_check: Piece.Piece, pieces_in_play: list[Piece.Piece], sprites_in_play):
    """Finds moves for the checked king to move to to evade check.

    Args:
        king_in_check (Piece.Piece): _description_
        pieces_in_play (list[Piece.Piece]): _description_
        sprites_in_play (_type_): _description_

    Returns:
        result (list[AvoidCheckPiece]): A list of AvoidCheckPiece - 
    """
    king_valid_moves = main.king_movement(pieces_in_play, king_in_check)

    result = []
    v = []  

    for king_vm in king_valid_moves:
        if not is_in_check(king_vm, king_in_check.colour, sprites_in_play):
            v.append(king_vm)

    result.append(AvoidCheckPiece.AvoidCheckPiece(king_in_check, v))    


    return result      





