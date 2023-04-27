import pygame
from win32api import GetSystemMetrics
import json
from types import SimpleNamespace
import square as Square
import rank as Rank
import piece_pixel_positions as Piece_pixel_positions
import piece as Piece
from typing import List
import main
import numpy as np

board = pygame.image.load("chessboard.png")

def update_squareInfojson(previous_square_name: str, moved_piece_rank: str, square_name: str):
    """Updates "pice_occupying" part of squareInfo.json

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
            json.dump(data, f)


    except Exception as e:
        print("Error: Unable to parse JSON data from file.")
        print("Details:", e)

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

def draw_piece_positions(screen: pygame.display, graphics: dict, piece_pixel_positions: List[Piece_pixel_positions.Piece_pixel_positions]): 

    """
    Adds pieces to their positions on the board.
    :param pygame.display screen: Screen to draw the images on.
    :param dictionary graphics: Dictionary containing piece name and its corresponding image.
    :param list of Piece_pixel_positions: List containing the colour, rank, x and y pixel positions.
    :return: none
    """

    for piece_pixel_position in piece_pixel_positions:
        piece_name = f"{piece_pixel_position.colour}_{piece_pixel_position.rank.name.lower()}"
        screen.blit(graphics[piece_name], [piece_pixel_position.x_pixel_position, piece_pixel_position.y_pixel_position])

def square_name_to_square_pixel_position(square_name: str):
    """Converts square name to the (top left x and y) pixel positions of the square

    Args:
        square_name (str): Name (e.g. 'a6')

    Returns:
        equivalent_pixel_positions (list): List of top left x and y pixel position of the square
    """

    squares = update_squares_from_json()

    for square in squares:
        if square.name == square_name:
            equivalent_pixel_positions = (square.top_left_x, square.top_left_y)

            return equivalent_pixel_positions

def find_current_piece_positions(squares: List[Piece_pixel_positions.Piece_pixel_positions]):  
    """Finds the piece pixel position (colour, top left x & y, rank) of each square in squares

    Args:
        squares (List[Piece_pixel_positions.Piece_pixel_positions]): List of piece pixel positions

    Returns:
        result (list of Piece_pixel_position): A list of piece pixel positions for squares
    """

    result = []
    x_cells = ["a", "b", "c", "d", "e", "f", "g", "h"]
    y_cells = [1, 2, 3, 4, 5, 6, 7, 8]

    for x in x_cells:
        for y in y_cells:
            p = main.get_piece_in_the_square(x, y, pieces_in_play)
            if p is not None:
                for square in squares: # squares needs to come from json
                    if square.name[0] == x and square.name[1] == str(y):
                        result.append(Piece_pixel_positions.Piece_pixel_positions(p.colour, square.top_left_x, square.top_left_y, p.rank))

    return result
    
def dictionary_to_object(data_dict: dict):  
    """Turns dictionaries into objects

    Args:
        data_dict (dict): A dictionary containing the properties of a square as keys and values (e.g. 'name': 'a6' ).

    Returns:
        square (Square): Info about a particular square on the board
    """
    square = Square.Square(data_dict["top_left_x"], data_dict["top_left_y"], data_dict["bottom_right_x"], data_dict["bottom_right_y"], data_dict["name"], data_dict["piece_occupying"])

    return square 

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
        squares.append(dictionary_to_object(square))

    

    return squares

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
            
def perform_black_turn(pieces_in_play: list): 
     
    pygame.image.save(screen, "current_view.png")
    has_completed_turn = False

    f = open('squareInfo.json')
    data_dictionary = json.load(f)
    f.close()

    squares = []

    for square in data_dictionary["squares"]:
            squares.append(dictionary_to_object(square))
    
    
    #selected_piece = main.get_piece_in_the_square(clicked_square[0], int(clicked_square[1]), pieces_in_play)
    #last_clicked_piece = selected_piece
    #valid_moves = get_movement_of_selected_piece(selected_piece)
       # highlight_squares(valid_moves)

    while not has_completed_turn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_position = pygame.mouse.get_pos()
                clicked_square = find_clicked_square(clicked_position, squares)
                selected_piece = main.get_piece_in_the_square(clicked_square[0], int(clicked_square[1]), pieces_in_play)

               
                # Player has clicked on a piece
                if main.get_piece_in_the_square(clicked_square[0], clicked_square[1], pieces_in_play) is not None:
                    selected_piece = main.get_piece_in_the_square(clicked_square[0], clicked_square[1], pieces_in_play)
                    last_clicked_piece = selected_piece
                    last_clicked_pixel_positions = clicked_position
                    valid_moves = get_movement_of_selected_piece(selected_piece)

                    unhighlighted_view_of_board = pygame.image.load("current_view.png")
                    screen.blit(unhighlighted_view_of_board, [0, 0])
                    pygame.display.flip()
                    highlight_squares(valid_moves)
                # Player has clicked on a highlighted square
                elif clicked_square in valid_moves:
                    screen.blit(graphics["board"], [0, 0])
                    pygame.display.flip()
                    
                    # for s in squares:
                    #     print(f"Name: {s.name}")
                    #     print(f"Piece occupying:{s.piece_occupying}")
                    update_squareInfojson(find_clicked_square(last_clicked_pixel_positions, squares), last_clicked_piece.rank.name.lower(), clicked_square)
                    squares = update_squares_from_json()
                    print("------------------------------------------------------------------------------------")
                    #for s in squares:
                        # print(f"Name: {s.name}")
                        # print(f"Piece occupying:{s.piece_occupying}")
                    #print(f"{last_clicked_piece.x_position}{last_clicked_piece.y_position}")
                    # create new non-clicked squares list
                    non_clicked_squares = []
                    for i in range(64):
                        if last_clicked_piece.x_position != squares[i].name[0]:
          #                  if last_clicked_piece.y_position != squares[i].name[1]:
                            non_clicked_squares.append(squares[i])
                            print(squares[i].name)
                    # for square in squares:
                    #     if square.name != last_clicked_piece.x_position + str(last_clicked_piece.y_position):
                    #         non_clicked_squares.append(square)
                    current_piece_positions = find_current_piece_positions(non_clicked_squares)
                    draw_piece_positions(screen, graphics, current_piece_positions)

                    piece_name = f"{last_clicked_piece.colour}_{last_clicked_piece.rank.name.lower()}"
                    last_clicked_piece_pixel_position = square_name_to_square_pixel_position(clicked_square)
                    screen.blit(graphics[piece_name], [last_clicked_piece_pixel_position[0], last_clicked_piece_pixel_position[1]])

                    pygame.display.update()
                    pygame.image.save(screen, "current_view.png")
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
squares = update_squares_from_json()
graphics = load_graphics()
last_clicked_piece = None

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
        perform_black_turn(pieces_in_play)

        # if event.type == pygame.MOUSEBUTTONUP:
        #     clicked_position = pygame.mouse.get_pos()
        #     print(clicked_position)
        #     print(find_clicked_square(clicked_position, squares))    
        #     clicked_square = find_clicked_square(clicked_position, squares)
        #     while not is_game_over:
        #         if not is_white_turn:
        #             perform_black_turn(clicked_square, pieces_in_play)
        #         else:
        #             perform_white_turn(clicked_square, pieces_in_play)
            