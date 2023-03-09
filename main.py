import numpy as np
import piece as Piece
import rank as Rank
from typing import List


def create_grid():
    """
    Uses an array to create the positions of all 64 squares of the chessboard
    :return:
    """

    cols = ["-", "-", "-", "-", "-", "-", "-", "-"]
    rows = ["-", "-", "-", "-", "-", "-", "-", "-"]
    grid = []

    for row in rows:
        new_row = []
        for col in cols:
            new_row.append(f"{col}{row}")
        grid.append(new_row)

    return np.asarray(grid)


def reset_pieces(grid):
    """
    Returns the grid with all the pieces on the grid in their starting positions.
    :param grid:
    :return:
    """

    grid[7][0] = "rw"
    grid[7][1] = "kw"
    grid[7][2] = "bw"
    grid[7][3] = "qw"
    grid[7][4] = "kw"
    grid[7][5] = "bw"
    grid[7][6] = "kw"
    grid[7][7] = "rw"

    for i, val in enumerate(grid[6]):
        grid[6][i] = "pw"

    grid[0][0] = "rb"
    grid[0][1] = "kb"
    grid[0][2] = "bb"
    grid[0][3] = "qb"
    grid[0][4] = "kb"
    grid[0][5] = "bb"
    grid[0][6] = "kb"
    grid[0][7] = "rb"

    for i, val in enumerate(grid[1]):
        grid[1][i] = "pb"

    return grid


def create_pieces():
    """
    Called once at the start of the game.
    :return: A list of pieces.
    """
    pieces = []
    possible_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

    piece_options = [["white", "b", 1, 2], ["white", "g", 1, 2], ["white", "c", 1, 3], ["white", "f", 1, 3],
                     ["white", "a", 1, 4],
                     ["white", "h", 1, 4], ["black", "b", 8, 2], ["black", "g", 8, 2], ["black", "c", 8, 3],
                     ["black", "f", 8, 3],
                     ["black", "a", 8, 4], ["black", "h", 8, 4]]

    for option in piece_options:
        pieces.append(two_of_a_kind_pieces(option[0], option[1], option[2], option[3]))

    # Black Pawn setup
    for i in range(8):
        piece = Piece.Piece("black", possible_columns[i], 7, Rank.Rank(1), 0)
        pieces.append(piece)
    # Black Queen setup
    pieces.append(Piece.Piece("black", "d", 8, Rank.Rank(5), 0))
    # Black King setup
    pieces.append(Piece.Piece("black", "e", 8, Rank.Rank(6), 0))

    # White Pawn setup
    for i in range(8):
        piece = Piece.Piece("white", possible_columns[i], 2, Rank.Rank(1), 0)
        pieces.append(piece)
    # White Queen setup
    pieces.append(Piece.Piece("white", "d", 1, Rank.Rank(5), 0))
    # White King setup
    pieces.append(Piece.Piece("white", "e", 1, Rank.Rank(6), 0))

    return pieces


def two_of_a_kind_pieces(colour, x_coordinate, y_coordinate, rank):
    """
    Creates the piece object for every rank that has two of each piece.
    :param string colour: Colour of the piece can be black or white.
    :param string x_coordinate: x coordinate of the piece, a-g inclusive.
    :param string y_coordinate: y coordinate of the piece, 1-8 inclusive.
    :param int rank: Rank of the piece, defined in the Rank enum.
    :return:piece object defined by the given arguments.
    """
    piece = Piece.Piece(colour, x_coordinate, y_coordinate, Rank.Rank(rank), 0)
    return piece


def examine_x_positions(letter, number):
    """
    Handles adding a number to a letter.
    :param string letter: The letter we want to add a number to.
    :param int number: The number we want to add (positive) or subtract (negative) to the letter.
    :return: string The result of adding the number to the letter.
    """
    letters_numbers_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

    if letters_numbers_dict[letter.lower()] + number > 8:
        return False
    if letters_numbers_dict[letter.lower()] + number < 1:
        return False

    number_result = letters_numbers_dict[letter.lower()] + number

    letter_result = list(letters_numbers_dict.keys())[list(letters_numbers_dict.values()).index(number_result)]

    return letter_result


def is_square_valid(x_square_pos, y_square_pos):
    if 1 <= converts_letter_to_number(x_square_pos) <= 8 and 1 <= y_square_pos <= 8 :
        return True
    return False


def converts_letter_to_number(letter):
    letters_numbers_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

    return letters_numbers_dict[letter.lower()]


def is_square_occupied(pieces: List[Piece.Piece] , x_square_pos: str, y_square_pos: int):
    """
    Checks if the given squares are occupied by any of the pieces.
    :param list pieces:  List of piece. A list of all the pieces currently on the board.
    :param string x_square_pos:  The x-coordinate of the piece.
    :param int y_square_pos: The x-coordinate of the piece.
    :return: bool True if the square is occupied by a piece, false otherwise.
    """
    for p in pieces:
        if x_square_pos == p.x_position and y_square_pos == p.y_position:
            return True
    return False


def get_piece_in_the_square(x_position, y_position, pieces) -> Piece.Piece: 
    """
    Checks if the given squares are occupied by any of the pieces, then returns the piece occupying it.
    :param string x_position:  The x-coordinate of the piece.
    :param int y_position: The x-coordinate of the piece.
    :param list pieces:  List of piece. A list of all the pieces currently on the board.
    :return: piece: The piece occupying the square.
    """
    if is_square_occupied(pieces, x_position, int(y_position)):
        for piece in pieces:
            if x_position == piece.x_position and int(y_position) == piece.y_position:
                return piece
    else:
        return None


def pawn_movement(pieces, piece):
    """
    Describes all pawn movement and adds them to a list of valid moves.
    :param list pieces: A list of all the pieces currently on the board.
    :param piece: The item of list pieces that pawn_movement is currently finding valid moves for.
    :return: valid_moves: A list of all the valid pawn moves for the player in that position.
    """
    valid_moves = []
    colour = piece.colour
    # TODO Implement en passant.
    # TODO Check diagonals at edges.
    # TODO Implement pawn promotion for when it reaches the opposite end of the board.
    if colour.lower() == "black":
        # Is the square in front blocked
        if is_square_occupied(pieces, piece.x_position, piece.y_position - 1):
            _ = 1  # something needs to happen here that isn't adding to the valid_moves array
        else:
            valid_moves.append(f"{piece.x_position}{piece.y_position - 1}")

        # Are the two squares in front of it blocked
        if not is_square_occupied(pieces, piece.x_position, piece.y_position - 1):
            if is_square_occupied(pieces, piece.x_position, piece.y_position - 2) and piece.move_counter == 0:
                _ = 1  # something needs to happen here that isn't adding to the valid_moves array
            else:
                valid_moves.append(f"{piece.x_position}{piece.y_position - 2}")

        # Is there a piece to take
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position - 1) \
                and get_piece_in_the_square(examine_x_positions(piece.x_position, -1), piece.y_position - 1,
                                            pieces).colour != piece.colour:
            # This is down and left
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position - 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position - 1) \
                and get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position - 1,
                                            pieces).colour != piece.colour:
            # This is down and right
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position - 1}")

    if colour.lower() == "white":
        # Is the square in front blocked
        if is_square_occupied(pieces, piece.x_position, piece.y_position + 1):
            _ = 1  # something needs to happen here that isn't adding to the valid_moves array
        else:
            valid_moves.append(f"{piece.x_position}{piece.y_position + 1}")

        # Are the two squares in front of it blocked
        if not is_square_occupied(pieces, piece.x_position, piece.y_position + 1):
            if not is_square_occupied(pieces, piece.x_position, piece.y_position + 2) and piece.move_counter == 0:
                valid_moves.append(f"{piece.x_position}{piece.y_position + 2}")
            else:
                _ = 1  # something needs to happen here that isn't adding to the valid_moves array

        # Is there a piece to take
        # This is up and left
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position + 1) \
                and get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position + 1, pieces).colour != piece.colour:
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position + 1}")
        # This is up and right
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position + 1) \
                and get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position + 1, pieces).colour != piece.colour:
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position + 1}")

    # If two valid moves are vertically above each other and the move_counter > 0, we need to remove the move that is
    # the furthest away from the piece.
    vertical_moves = []
    for move in valid_moves:
        if move[0] == piece.y_position:
            vertical_moves.append(move)

    # removes invalid moves from the list valid_moves.
    invalid_moves = []
    for move in valid_moves:
        if move[1] == "-" or move[1] == "0" or int(move[1:]) > 8:
            invalid_moves.append(move)
        elif move[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            invalid_moves.append(move)
    for move in invalid_moves:
        valid_moves.remove(move)



    return valid_moves


def knight_movement(pieces, piece):
    valid_moves = []
    
    # +2 y_pos, +1 x_pos
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position + 2) and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position + 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position + 2}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position + 2) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position + 2, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position + 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position + 2}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # +2 y_pos, -1 x_pos
    if examine_x_positions(piece.x_position, -1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position + 2) and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position + 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position + 2}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position + 2) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -1), piece.y_position + 2, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position + 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position + 2}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # -2 y_pos, +1 x_pos
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position - 2) and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position - 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position - 2}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position - 2) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position - 2, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position - 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position - 2}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # -2 y_pos, -1 x_pos
    if examine_x_positions(piece.x_position, -1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position - 2) and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position - 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position - 2}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position - 2) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -1), piece.y_position - 2, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position - 2):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position - 2}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # +1 y_pos, +2 x_pos
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 2), piece.y_position + 1) and \
                is_square_valid(examine_x_positions(piece.x_position, 2), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 2)}{piece.y_position + 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 2), piece.y_position + 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 2), piece.y_position + 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 2), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 2)}{piece.y_position + 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # +1 y_pos, -2 x_pos
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -2), piece.y_position + 1) and \
                is_square_valid(examine_x_positions(piece.x_position, -2), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -2)}{piece.y_position + 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -2), piece.y_position + 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -2), piece.y_position + 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -2), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -2)}{piece.y_position + 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # -1 y_pos, +2 x_pos
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 2), piece.y_position - 1) and \
                is_square_valid(examine_x_positions(piece.x_position, 2), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 2)}{piece.y_position - 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 2), piece.y_position - 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 2), piece.y_position - 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 2), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 2)}{piece.y_position - 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # -1 y_pos, -2 x_pos
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -2), piece.y_position - 1) and \
                is_square_valid(examine_x_positions(piece.x_position, -2), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -2)}{piece.y_position - 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -2), piece.y_position - 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -2), piece.y_position - 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -2), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -2)}{piece.y_position - 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # removes invalid moves from the list valid_moves.
    invalid_moves = []
    for move in valid_moves:
        if move[1] == "-" or move[1] == "0" or int(move[1:]) > 8:
            invalid_moves.append(move)
        elif move[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            invalid_moves.append(move)
    for move in invalid_moves:
        valid_moves.remove(move)

    return valid_moves


def rook_movement(pieces, piece):
    # TODO: castling
    valid_moves = []

  #  if piece.colour.lower() == "black":
    # up/y_position increasing
    squares_to_top = 8 - piece.y_position
    for i in range(1, squares_to_top + 1):
        if not is_square_occupied(pieces, piece.x_position, piece.y_position + i):
            valid_moves.append(f"{piece.x_position}{piece.y_position + i}")
        else:
            if piece.colour == get_piece_in_the_square(piece.x_position, piece.y_position + i, pieces).colour:
                break
            else:
                valid_moves.append(f"{piece.x_position}{piece.y_position + i}")
                break
    # down/y_position decreasing
    squares_to_bottom = piece.y_position - 1
    for i in range(1, squares_to_bottom + 1):
        if not is_square_occupied(pieces, piece.x_position, piece.y_position - i):
            valid_moves.append(f"{piece.x_position}{piece.y_position - i}")
        else:
            if piece.colour == get_piece_in_the_square(piece.x_position, piece.y_position - i, pieces).colour:
                break
            else:
                valid_moves.append(f"{piece.x_position}{piece.y_position - i}")
                break
    # left/x_position decreasing
    squares_to_column_a = converts_letter_to_number(piece.x_position) - 1
    for i in range(1, squares_to_column_a + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i),
                                                       piece.y_position, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position}")
                break
    # right/x_position increasing
    squares_to_column_h = 8 - converts_letter_to_number(piece.x_position)
    for i in range(1, squares_to_column_h + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i), piece.y_position, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position}")
                break

    # removes invalid moves from the list valid_moves.
    invalid_moves = []
    for move in valid_moves:
        if move[1] == "-" or move[1] == "0" or int(move[1:]) > 8:
            invalid_moves.append(move)
        elif move[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            invalid_moves.append(move)
    for move in invalid_moves:
        valid_moves.remove(move)

    return valid_moves


def king_movement(pieces, piece):
    # TODO: castling
    valid_moves = []

# if piece.colour.lower() == "white":
    # up
    if not is_square_occupied(pieces, piece.x_position, piece.y_position + 1) \
            and is_square_valid(piece.x_position, piece.y_position + 1):
        valid_moves.append(f"{piece.x_position}{piece.y_position + 1}")
    if is_square_occupied(pieces, piece.x_position, piece.y_position + 1) and \
            get_piece_in_the_square(piece.x_position, piece.y_position + 1, pieces).colour != piece.colour.lower() and \
            is_square_valid(piece.x_position, piece.y_position + 1):
        valid_moves.append(f"{piece.x_position}{piece.y_position + 1}")
    else:
        _ = 1  # something needs to happen here that isn't adding to valid_moves

    # down
    if not is_square_occupied(pieces, piece.x_position, piece.y_position - 1) and \
            is_square_valid(piece.x_position, piece.y_position - 1):
        valid_moves.append(f"{piece.x_position}{piece.y_position - 1}")
    if is_square_occupied(pieces, piece.x_position, piece.y_position - 1) and \
            get_piece_in_the_square(piece.x_position, piece.y_position - 1, pieces).colour != piece.colour.lower() and \
            is_square_valid(piece.x_position, piece.y_position - 1):
        valid_moves.append(f"{piece.x_position}{piece.y_position - 1}")
    else:
        _ = 1  # something needs to happen here that isn't adding to valid_moves

    # left
    if examine_x_positions(piece.x_position, -1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position) and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -1), piece.y_position, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # right
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position) and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # diagonally up and right
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position + 1) and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position + 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position + 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position + 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position + 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # diagonally up and left
    if examine_x_positions(piece.x_position, -1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position + 1) and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position + 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position + 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -1), piece.y_position + 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position + 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position + 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # diagonally down and right
    if examine_x_positions(piece.x_position, 1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position - 1) and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position - 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position - 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position - 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, 1), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position - 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # diagonally down and left
    if examine_x_positions(piece.x_position, -1) != False:  # examine_x_positions returns false if the position is off the board
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position - 1) and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position - 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position - 1) and \
                get_piece_in_the_square(examine_x_positions(piece.x_position, -1), piece.y_position - 1, pieces).colour != piece.colour.lower() and \
                is_square_valid(examine_x_positions(piece.x_position, -1), piece.y_position - 1):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position - 1}")
        else:
            _ = 1  # something needs to happen here that isn't adding to valid_moves

    # removes invalid moves from the list valid_moves.
    invalid_moves = []
    for move in valid_moves:
        if move[1] == "-" or move[1] == "0" or int(move[1:]) > 8:
            invalid_moves.append(move)
        elif move[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            invalid_moves.append(move)
    for move in invalid_moves:
        valid_moves.remove(move)

    return valid_moves


def bishop_movement(pieces, piece):
    valid_moves = []
    squares_to_top = 8 - piece.y_position
    squares_to_bottom = piece.y_position - 1
    squares_to_column_a = converts_letter_to_number(piece.x_position) - 1
    squares_to_column_h = 8 - converts_letter_to_number(piece.x_position)

    # up and right
    number_of_diagonals_to_edge = min(squares_to_top, squares_to_column_h)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position + i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position + i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i), piece.y_position + i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position + i}")
                break
    # down and right
    number_of_diagonals_to_edge = min(squares_to_bottom, squares_to_column_h)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position - i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position - i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i),
                                                       piece.y_position - i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position - i}")
                break
    # down and left
    number_of_diagonals_to_edge = min(squares_to_bottom, squares_to_column_a)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position - i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position - i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i),
                                                       piece.y_position - i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position - i}")
                break
    # up and left
    number_of_diagonals_to_edge = min(squares_to_top, squares_to_column_a)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position + i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position + i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i),
                                                       piece.y_position + i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position + i}")
                break

    # removes invalid moves from the list valid_moves.
    invalid_moves = []
    for move in valid_moves:
        if move[1] == "-" or move[1] == "0" or int(move[1:]) > 8:
            invalid_moves.append(move)
        elif move[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            invalid_moves.append(move)
    for move in invalid_moves:
        valid_moves.remove(move)

    return valid_moves


def queen_movement(pieces, piece):

    valid_moves = []

    # STRAIGHT
    # up
    squares_to_top = 8 - piece.y_position
    for i in range(1, squares_to_top + 1):
        if not is_square_occupied(pieces, piece.x_position, piece.y_position + i):
            valid_moves.append(f"{piece.x_position}{piece.y_position + i}")
        else:
            if piece.colour == get_piece_in_the_square(piece.x_position, piece.y_position + i, pieces).colour:
                break
            else:
                valid_moves.append(f"{piece.x_position}{piece.y_position + i}")
                break
    # down
    squares_to_bottom = piece.y_position - 1
    for i in range(1, squares_to_bottom + 1):
        if not is_square_occupied(pieces, piece.x_position, piece.y_position - i):
            valid_moves.append(f"{piece.x_position}{piece.y_position - i}")
        else:
            if piece.colour == get_piece_in_the_square(piece.x_position, piece.y_position - i, pieces).colour:
                break
            else:
                valid_moves.append(f"{piece.x_position}{piece.y_position - i}")
                break
    # left
    squares_to_column_a = converts_letter_to_number(piece.x_position) - 1
    for i in range(1, squares_to_column_a + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i),
                                                       piece.y_position, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position}")
                break
    # right
    squares_to_column_h = 8 - converts_letter_to_number(piece.x_position)
    for i in range(1, squares_to_column_h + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position):
            valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i), piece.y_position, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position}")
                break
   
    # DIAGONALS
    squares_to_top = 8 - piece.y_position
    squares_to_bottom = piece.y_position - 1
    squares_to_column_a = converts_letter_to_number(piece.x_position) - 1
    squares_to_column_h = 8 - converts_letter_to_number(piece.x_position)

    # up and right
    number_of_diagonals_to_edge = min(squares_to_top, squares_to_column_h)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position + i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position + i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i), piece.y_position + i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position + i}")
                break
    # down and right
    number_of_diagonals_to_edge = min(squares_to_bottom, squares_to_column_h)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position - i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position - i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i),
                                                       piece.y_position - i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position - i}")
                break
    # down and left
    number_of_diagonals_to_edge = min(squares_to_bottom, squares_to_column_a)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position - i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position - i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i),
                                                       piece.y_position - i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position - i}")
                break
    # up and left
    number_of_diagonals_to_edge = min(squares_to_top, squares_to_column_a)
    for i in range(1, number_of_diagonals_to_edge + 1):
        if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position + i):
            valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position + i}")
        else:
            if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i),
                                                       piece.y_position + i, pieces).colour:
                break
            else:
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position + i}")
                break


    # removes invalid moves from the list valid_moves.
    invalid_moves = []
    for move in valid_moves:
        if move[1] == "-" or move[1] == "0" or int(move[1:]) > 8:
            invalid_moves.append(move)
        elif move[0] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            invalid_moves.append(move)
    for move in invalid_moves:
        valid_moves.remove(move)

    return valid_moves



if __name__ == '__main__':
    grid = create_grid()
    initial_position_grid = reset_pieces(grid)
    print(initial_position_grid)
    pieces = create_pieces()

    all_pawns = []
    for piece in pieces:
        if piece.rank == Rank.Rank.pawn:
            all_pawns.append(piece)

        all_other_pawns = [p for p in all_pawns if p.x_position != piece.x_position or p.y_position != piece.y_position]

        if piece.rank == Rank.Rank.pawn:
            moves = pawn_movement(all_other_pawns, piece)

