import piece as Piece
import rank as Rank
import clickable_sprite as ClickableSprite
from typing import List
import helpers
import main


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


def find_pieces_to_take_checking_piece(king_in_check: Piece.Piece, piece_checking_king: Piece.Piece, pieces_in_play: list[Piece.Piece]):
    pieces_that_can_take = []
    
    for piece in pieces_in_play:
        if piece.colour != piece_checking_king.colour:
            piece_valid_moves = helpers.get_valid_moves(piece)
            for valid_move in piece_valid_moves:
                if valid_move == piece_checking_king:
                    pieces_that_can_take.append(piece)
                    
    return pieces_that_can_take 

def find_pieces_to_block_check(king_in_check: Piece.Piece, piece_checking_king: Piece.Piece, pieces_in_play: list[Piece.Piece]): 
    pieces_to_block = []
    # piece_blocking_valid_moves = [] # this is sprite_valid_moves for the loop i guess
    # piece_checking_king_valid_moves = []
    all_valid_moves = {}
    king_in_check_x, piece_checking_king_x = main.converts_letter_to_number(king_in_check.x_position),  main.converts_letter_to_number(piece_checking_king.x_position)
    x_result = piece_checking_king_x - king_in_check_x
    y_result = piece_checking_king.y_position - king_in_check.y_position    
    for piece in pieces_in_play:
        if piece.colour != piece_checking_king.colour:
            piece_valid_moves = helpers.get_valid_moves_for_piece_object(piece) # list of valid moves for piece
            all_valid_moves.update({piece : piece_valid_moves})
            

    if piece_checking_king.rank == Rank.Rank.knight.value or piece_checking_king.rank == Rank.Rank.pawn.value:
        print("impossible to block sorry")
        return None
    else:
        #PIECE CHECKING KING == ROOK - DONE!
        if piece_checking_king.rank == Rank.Rank.rook.value:
            #ROOK X_POS
            if king_in_check.x_position == piece_checking_king.x_position:
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                            if vm[0] == king_in_check.x_position:
                                pieces_to_block.append(piece)     
            #ROOK Y_POS
            elif king_in_check.y_position == piece_checking_king.y_position:
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                            if vm[1] == king_in_check.y_position:
                                pieces_to_block.append(piece)             
        # BISHOP 
        elif piece_checking_king.rank == Rank.Rank.bishop.value:
            if x_result == y_result:
                diagonal_vms = helpers.get_valid_moves(piece_checking_king) 
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                            if vm in diagonal_vms:
                                pieces_to_block.append(piece)      
        # QUEEN 
        elif piece_checking_king.rank == Rank.Rank.queen.value:
            #QUEEN DIAGONAL
            if x_result == y_result:
                diagonal_vms = helpers.get_valid_moves(piece_checking_king)
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                            if vm in diagonal_vms:
                                pieces_to_block.append(piece) 
            #QUEEN STRAIGHT
            # X_POS
            if king_in_check.x_position == piece_checking_king.x_position:
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                            if vm[0] == king_in_check.x_position:
                                pieces_to_block.append(piece)     
            # Y_POS
            elif king_in_check.y_position == piece_checking_king.y_position:
                for piece, piece_valid_moves in all_valid_moves.items():
                    for vm in piece_valid_moves:
                            if vm[1] == king_in_check.y_position:
                                pieces_to_block.append(piece)    

    return pieces_to_block      

def run_to_avoid_checkmate():
    #TODO: Write method
    return            

        



