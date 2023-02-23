import pygame
from win32api import GetSystemMetrics
import json
from types import SimpleNamespace
import square as Square
from typing import List

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
    square = Square.Square(data_dict["top_left_x"], data_dict["top_left_y"], data_dict["bottom_right_x"], data_dict["bottom_right_y"], data_dict["name"], data_dict["piece_occupying"])

    return square 

def initialize_squares():
    squares = []

    f = open('squareInfo.json')
    data_dictionary = json.load(f)
    f.close()

    for square in data_dictionary["squares"]:
        squares.append(dictionary_to_object(square))

    return squares

def find_clicked_square(coordinates: tuple, squares: List[Square.Square] ):
    #TODO: If user clicks outside grid 
    for square in squares:
        if coordinates[0] > square.top_left_x and coordinates[0] < square.bottom_right_x and \
         coordinates[1] > square.top_left_y and coordinates[1] < square.bottom_right_y:
            return square.name

def highlight_squares():
    return

            
def perform_white_turn(clicked_square: str):
    is_white_turn = False
    return
def perform_black_turn(clicked_square: str):
    is_white_turn = True
    return

is_white_turn = True
is_game_over = False
squares = initialize_squares()
graphics = load_graphics()

background_colour = (0, 150, 250)
#(width, height) = (0.9*GetSystemMetrics(0), 0.9*GetSystemMetrics(1))
(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
highlight_surface_layer = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")
screen.fill(background_colour)
s = pygame.Surface((1000,750))  # the size of your rect
s.set_alpha(50)                # alpha level
s.fill((255,255,255))           # this fills the entire surface
pygame.display.flip()
running = True
while running:
    screen.blit(board, [0, 0])
    highlight_surface_layer.blit(s, (0,0))    # (0,0) are the top-left coordinates

    starting_positions(screen, graphics)
    pygame.draw.rect(screen, (54, 152, 200, 0), (20, 150, 240, 240))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked_position = pygame.mouse.get_pos()
           # print(clicked_position)
            # print(find_clicked_square(clicked_position, squares))    
            clicked_square = find_clicked_square(clicked_position, squares)
    # while not is_game_over:
    #     if is_white_turn:
    #         perform_white_turn(clicked_square)
    #     else:
    #         perform_black_turn(clicked_square)
    