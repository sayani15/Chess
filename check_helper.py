import piece as Piece
import rank as Rank
import AvoidCheckPiece as AvoidCheckPiece
import clickable_sprite as ClickableSprite
from typing import List
import helpers
import main
import numpy as np


def is_in_check(king_to_be_checked_position: str, colour_to_be_checked: str, sprites_in_play: list[ClickableSprite.ClickableSprite]):
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
    pieces_that_can_take = []
    
    for piece in pieces_in_play:
        if piece.colour != piece_checking_king.colour:
            piece_valid_moves = helpers.get_valid_moves_for_piece_object(piece, pieces_in_play)
            for valid_move in piece_valid_moves:
                if valid_move == f"{piece_checking_king.x_position}{piece_checking_king.y_position}":
                    pieces_that_can_take.append(AvoidCheckPiece.AvoidCheckPiece(piece, [valid_move]))   #TODO: Verify that there will only ever be one valid move
                    
    return pieces_that_can_take 

def find_pieces_to_block_check(king_in_check: Piece.Piece, piece_checking_king: Piece.Piece, pieces_in_play: list[Piece.Piece]): 
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
    
    partial_result = []     
    for piece in pieces_to_enable_blocking:
        partial_result.append(AvoidCheckPiece.AvoidCheckPiece(piece, all_valid_moves[piece]))

    result = []

    #filters the relevant valid moves from the useless ones
    for r in partial_result:
        vms = []
        for v in r.valid_moves:
            if v in squares_to_block_check:   
                vms.append(v)
        result.append(AvoidCheckPiece.AvoidCheckPiece(r.piece, vms)) 
               
    

    return result   

def run_to_avoid_checkmate(king_in_check: Piece.Piece, piece_checking_king: Piece.Piece, pieces_in_play: list[Piece.Piece]):
    all_valid_moves = {}
    king_valid_moves = main.king_movement(pieces_in_play, king_in_check)

    for piece in pieces_in_play:
        if piece.colour != piece_checking_king.colour and piece.rank != king_in_check.rank:
            piece_valid_moves = helpers.get_valid_moves_for_piece_object(piece, pieces_in_play) # list of valid moves for piece
            all_valid_moves.update({piece : piece_valid_moves})

    result = []
    v = []
    for vm in king_valid_moves:
        for i in all_valid_moves.values():
            if vm != i:
                v.append(vm)
    result.append(AvoidCheckPiece.AvoidCheckPiece(king_in_check, v))    

    return result      





