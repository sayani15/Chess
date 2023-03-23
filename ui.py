import pygame
from win32api import GetSystemMetrics
import json
from types import SimpleNamespace
import square as Square
import rank as Rank
import piece as Piece
from typing import List
import main
import numpy as np

board = pygame.image.load("chessboard.png")

def load_graphics():
    """Loads the images from the file.

    Returns:
        Dictionary:  Dictionary containing piece name and its corresponding image.
    """
    result = {}
    #background
    result["board"] = pygame.image.load("chessboard.png")

    #black pieces
    result["black_pawn"] = pygame.image.load("Pieces\\black\\pawn.png")
    
    result["black_knight"] = pygame.image.load("Pieces\\black\\knight.png")

    result["black_bishop"] = pygame.image.load("Pieces\\black\\bishop.png")

    result["black_rook"] = pygame.image.load("Pieces\\black\\rook.png")

    result["black_queen"] = pygame.image.load("Pieces\\black\\queen.png")

    result["black_king"] = pygame.image.load("Pieces\\black\\king.png")

    #white pieces
    result["white_pawn"] = pygame.image.load("Pieces\\white\\pawn.png")
    
    result["white_knight"] = pygame.image.load("Pieces\\white\\knight.png")

    result["white_bishop"] = pygame.image.load("Pieces\\white\\bishop.png")

    result["white_rook"] = pygame.image.load("Pieces\\white\\rook.png")

    result["white_queen"] = pygame.image.load("Pieces\\white\\queen.png")

    result["white_king"] = pygame.image.load("Pieces\\white\\king.png")


    return result

def starting_positions(screen: pygame.display, graphics: dict):

    """
    Adds pieces to their starting positions on the board.
    :param pygame.display screen: Screen to draw the images on.
    :param dictionary graphics: Dictionary containing piece name and its corresponding image.
    :return: none
    """
    screen.blit(graphics["black_pawn"], [26, 87])
    screen.blit(graphics["black_pawn"], [97, 87])
    screen.blit(graphics["black_pawn"], [165, 87])
    screen.blit(graphics["black_pawn"], [224, 87])
    screen.blit(graphics["black_pawn"], [295, 87])
    screen.blit(graphics["black_pawn"], [358, 87])
    screen.blit(graphics["black_pawn"], [430, 87])
    screen.blit(graphics["black_pawn"], [489, 87])

    screen.blit(graphics["black_rook"], [31, 17])
    screen.blit(graphics["black_rook"], [500, 17])

    screen.blit(graphics["black_knight"], [97, 17])
    screen.blit(graphics["black_knight"], [430, 17])

    screen.blit(graphics["black_bishop"], [161, 17])
    screen.blit(graphics["black_bishop"], [365, 17])

    screen.blit(graphics["black_queen"], [230, 17])
    screen.blit(graphics["black_king"], [295, 17])


    screen.blit(graphics["white_pawn"], [26, 428])
    screen.blit(graphics["white_pawn"], [97, 428])
    screen.blit(graphics["white_pawn"], [165, 428])
    screen.blit(graphics["white_pawn"], [224, 428])
    screen.blit(graphics["white_pawn"], [295, 428])
    screen.blit(graphics["white_pawn"], [358, 428])
    screen.blit(graphics["white_pawn"], [430, 428])
    screen.blit(graphics["white_pawn"], [489, 428])

    screen.blit(graphics["white_rook"], [31, 490])
    screen.blit(graphics["white_rook"], [500, 490])

    screen.blit(graphics["white_knight"], [97, 490])
    screen.blit(graphics["white_knight"], [430, 490])

    screen.blit(graphics["white_bishop"], [161, 490])
    screen.blit(graphics["white_bishop"], [365, 490])

    screen.blit(graphics["white_queen"], [230, 490])
    screen.blit(graphics["white_king"], [295, 490])

def dictionary_to_object(data_dict: dict):
    """TUrns dictionaries into objects

    Args:
        data_dict (dict): 

    Returns:
        square (): _description_
    """
    square = Square.Square(data_dict["top_left_x"], data_dict["top_left_y"], data_dict["bottom_right_x"], data_dict["bottom_right_y"], data_dict["name"], data_dict["piece_occupying"])

    return square 

def initialize_squares():
    """Adds info about each square from the json file to square

    Returns:
        squares (list): List of square
    """
    squares = []

    f = open('squareInfo.json')
    data_dictionary = json.load(f)
    f.close()

    for square in data_dictionary["squares"]:
        squares.append(dictionary_to_object(square))

    return squares

def find_clicked_square(coordinates: tuple, squares: List[Square.Square] ):
    """Finds the name of the square when given coordinates of position.

    Args:
        coordinates (tuple): List containing coordinates of position that has been clicked on 
        squares (List[Square.Square]): List of squares

    Returns:
        square.name (string): Name of square
    """
    #TODO: If user clicks outside grid 
    for square in squares:
        if coordinates[0] > square.top_left_x and coordinates[0] < square.bottom_right_x and \
         coordinates[1] > square.top_left_y and coordinates[1] < square.bottom_right_y:
            return square.name

def highlight_squares(valid_moves: List[str]):
    """Draws rectangles to highlight the squares that are part of the valid_moves for selected_piece.

    Args:
        squares (List[Square.Square]): A list of all squares
    """
    squares_to_highlight = []

    for valid_move in valid_moves:
        for square in squares:
            if square.name[0] == valid_move[0] and square.name[1] == valid_move[1]:
                squares_to_highlight.append(square)

    for square in squares_to_highlight:
        width = np.abs(square.bottom_right_x - square.top_left_x)
        height = np.abs(square.bottom_right_y - square.top_left_y)

        pygame.draw.rect(screen, (54, 152, 200, 0), (square.top_left_x, square.top_left_y, width, height))

    pygame.display.flip()

    return

def get_movement_of_selected_piece(selected_piece: Piece):
    """Finds the rank of the player's selected piece and returns the valid moves for the piece in its current position.

    Args:
        selected_piece (Piece): The piece that has been selected by the player.

    Raises:
        Exception: Raises exception if selected_piece's rank does not match a valid rank.

    Returns:
        valid_moves (list) : List of available moves for the piece.
    """
    if selected_piece.rank == Rank.Rank.pawn:
        valid_moves = main.pawn_movement(pieces_in_play, selected_piece)
    elif selected_piece.rank == Rank.Rank.knight:
        valid_moves = main.knight_movement(pieces_in_play, selected_piece)
    elif selected_piece.rank == Rank.Rank.bishop:
        valid_moves = main.bishop_movement(pieces_in_play, selected_piece)
    elif selected_piece.rank == Rank.Rank.rook:
        valid_moves = main.rook_movement(pieces_in_play, selected_piece)
    elif selected_piece.rank == Rank.Rank.queen:
        valid_moves = main.queen_movement(pieces_in_play, selected_piece)
    elif selected_piece.rank == Rank.Rank.king:
        valid_moves = main.king_movement(pieces_in_play, selected_piece)  
    else:
        raise Exception
    
    return valid_moves
            
def perform_black_turn(clicked_square: str, pieces_in_play: list):
    pygame.image.save(screen, "current_view.png")
    has_completed_turn = False
    selected_piece = main.get_piece_in_the_square(clicked_square[0], int(clicked_square[1]), pieces_in_play)

    valid_moves = get_movement_of_selected_piece(selected_piece)
    
    f = open('squareInfo.json')
    data_dictionary = json.load(f)
    f.close()

    squares.clear()

    for square in data_dictionary["squares"]:
            squares.append(dictionary_to_object(square))
    

    highlight_squares(valid_moves)

    while not has_completed_turn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_position = pygame.mouse.get_pos()
               
                clicked_square = find_clicked_square(clicked_position, squares)
                # Player has clicked on a different piece
                if main.get_piece_in_the_square(clicked_square[0], clicked_square[1], pieces_in_play) is not None:
                    selected_piece = main.get_piece_in_the_square(clicked_square[0], clicked_square[1], pieces_in_play)
                    valid_moves = get_movement_of_selected_piece(selected_piece)

                    unhighlighted_view_of_board = pygame.image.load("current_view.png")
                    screen.blit(unhighlighted_view_of_board, [0, 0])
                    pygame.display.flip()
                    highlight_squares(valid_moves)
                    a = 1 # write the method
                    
                # Player has clicked on a highlighted square
                elif clicked_square in valid_moves:
                    a = 1 # write the method
                # Player has clicked somewhere else
                else:
                    unhighlighted_view_of_board = pygame.image.load("current_view.png")
                    screen.blit(unhighlighted_view_of_board, [0, 0])
                    pygame.display.flip()



                    


    

        
    is_white_turn = False
    return

def perform_white_turn(clicked_square: str):
    is_white_turn = True
    return


is_white_turn = False   # TODO: Turn back to true when method's written
is_game_over = False
pieces_in_play = main.create_pieces()
squares = initialize_squares()
graphics = load_graphics()

background_colour = (0, 150, 250)
#(width, height) = (0.9*GetSystemMetrics(0), 0.9*GetSystemMetrics(1))
(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("chess")
screen.fill(background_colour)
rectangle_surface = pygame.Surface((1000,750))  # the size of your rect
rectangle_surface.set_alpha(70)                # alpha level
rectangle_surface.fill((255,255,255))           # this fills the entire surface
pygame.display.flip()

running = True

while running:
    screen.blit(board, [0, 0])
    screen.blit(rectangle_surface, [0, 0])

    starting_positions(screen, graphics)
    #pygame.draw.rect(screen, (54, 152, 200, 0), (20, 150, 240, 240))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked_position = pygame.mouse.get_pos()
            # print(clicked_position)
            # print(find_clicked_square(clicked_position, squares))    
            clicked_square = find_clicked_square(clicked_position, squares)
            while not is_game_over:
                if not is_white_turn:
                    perform_black_turn(clicked_square, pieces_in_play)
                else:
                    perform_white_turn(clicked_square, pieces_in_play)
            