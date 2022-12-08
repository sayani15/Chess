import numpy as np
import piece as Piece
import rank as Rank


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
        raise ValueError("Position is off the edge of the board.")

    if letters_numbers_dict[letter.lower()] + number < 1:
        raise ValueError("Position is off the edge of the board.")

    number_result = letters_numbers_dict[letter.lower()] + number

    letter_result = list(letters_numbers_dict.keys())[list(letters_numbers_dict.values()).index(number_result)]

    return letter_result


def is_square_occupied(pieces, x_square_pos, y_square_pos):
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


def get_piece_in_the_square(x_position, y_position, pieces):
    """
    Checks if the given squares are occupied by any of the pieces, then returns the piece occupying it.
    :param string x_position:  The x-coordinate of the piece.
    :param int y_position: The x-coordinate of the piece.
    :param list pieces:  List of piece. A list of all the pieces currently on the board.
    :return: piece: The piece occupying the square.
    """
    if is_square_occupied(pieces, x_position, y_position):
        for piece in pieces:
            if x_position == piece.x_position and y_position == piece.y_position:
                return piece
    else:
        raise Exception(f"Square {x_position},{y_position} not occupied.")


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
            if is_square_occupied(pieces, piece.x_position, piece.y_position + 2) and piece.move_counter == 0:
                _ = 1  # something needs to happen here that isn't adding to the valid_moves array
            else:
                valid_moves.append(f"{piece.x_position}{piece.y_position + 2}")
        # Is there a piece to take
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, -1), piece.y_position + 1) \
                and get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position + 1,
                                            pieces).colour != piece.colour:
            # This is up and left
            valid_moves.append(f"{examine_x_positions(piece.x_position, -1)}{piece.y_position + 1}")
        if is_square_occupied(pieces, examine_x_positions(piece.x_position, 1), piece.y_position + 1) \
                and get_piece_in_the_square(examine_x_positions(piece.x_position, 1), piece.y_position + 1,
                                            pieces).colour != piece.colour:
            # This is up and right
            valid_moves.append(f"{examine_x_positions(piece.x_position, 1)}{piece.y_position + 1}")

    # If two valid moves are vertically above each other and the move_counter > 0, we need to remove the move that is
    # the furthest away from the piece.
    vertical_moves = []
    for move in valid_moves:
        if move[0] == piece.y_position:
            vertical_moves.append(move)

    return valid_moves


def rook_movement(pieces, piece):
    valid_moves = []

    if piece.colour.lower() == "black":
        # y_position increasing
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
        # y_position decreasing
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
        # x_position increasing
        squares_to_column_h = examine_x_positions(piece.x_position, -8)
        for i in range(1, squares_to_column_h + 1):
            if not is_square_occupied(pieces, examine_x_positions(piece.x_position, i), piece.y_position):
                valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position}")
            else:
                if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, i), piece.y_position, pieces).colour:
                    break
                else:
                    valid_moves.append(f"{examine_x_positions(piece.x_position, i)}{piece.y_position}")
                    break
        # x_position decreasing
        squares_to_column_a = examine_x_positions(piece.x_position, -1)
        for i in range(1, squares_to_column_a + 1):
            if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -i), piece.y_position):
                valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position}")
            else:
                if piece.colour == get_piece_in_the_square(examine_x_positions(piece.x_position, -i), piece.y_position, pieces).colour:
                    break
                else:
                    valid_moves.append(f"{examine_x_positions(piece.x_position, -i)}{piece.y_position}")
                    break
    return valid_moves


        #         if not is_square_occupied(pieces, piece.x_position, piece.y_position + loop_counter) \
        #         and piece.y_position < 8:
        #     valid_moves.append(f"{piece.x_position}{piece.y_position + loop_counter}")
        # # y_position decreasing
        # if not is_square_occupied(pieces, piece.x_position, piece.y_position - loop_counter) \
        #         and piece.y_position > 1:
        #     valid_moves.append(f"{piece.x_position}{piece.y_position - loop_counter}")
        # # x_position increasing
        # if not is_square_occupied(pieces, examine_x_positions(piece.x_position, loop_counter), piece.y_position) \
        #         and piece.x_position < "h":
        #     valid_moves.append(f"{examine_x_positions(piece.x_position, loop_counter)}{piece.y_position}")
        # # x_position decreasing
        # if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -loop_counter), piece.y_position) \
        #         and piece.x_position > "a":
        #     valid_moves.append(f"{examine_x_positions(piece.x_position, -loop_counter)}{piece.y_position}")


# for piece in pieces:
#     loop_counter+=1
#     # x_position increasing
#     if not is_square_occupied(pieces, examine_x_positions(piece.x_position, loop_counter), piece.y_position)\
#             and loop_counter < 8-piece.x_position:
#         valid_moves.append(f"{examine_x_positions(piece.x_position, loop_counter)}{piece.y_position}")
#     # x_position decreasing
#     if not is_square_occupied(pieces, examine_x_positions(piece.x_position, -loop_counter), piece.y_position)\
#             and loop_counter < piece.x_position:
#         valid_moves.append(f"{examine_x_positions(piece.x_position, -loop_counter)}{piece.y_position}")
#     # y_position increasing
#     if not is_square_occupied(pieces, piece.x_position, piece.y_position + loop_counter)\
#             and loop_counter < 8-piece.y_position:
#         valid_moves.append(f"{piece.x_position}{piece.y_position + loop_counter}")
#     # y_position decreasing
#     if not is_square_occupied(pieces, piece.x_position, piece.y_position - loop_counter)\
#             and loop_counter < piece.y_position - 1:
#         valid_moves.append(f"{piece.x_position}{piece.y_position - loop_counter}")


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

