import pygame
import rank as Rank
import helpers
import square as Square
from typing import List
import piece as Piece
import main
import json
import numpy as np
import PieceSprite as ps


click_counter = 0
selected_sprite = None

class ClickableSprite(pygame.sprite.Sprite):
	def __init__(self, image_file_path: str, x: int, y: int, callback, colour: str, rank: Rank, move_counter: int):
		super().__init__()
		#self.image = image
		self.image = pygame.image.load(image_file_path)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.callback = callback
		self.colour = colour
		self.move_counter = 0
		self.rank = rank
		self.visible = True
		

	

	def movement(self, x: int, y: int):
		self.rect.x = x
		self.rect.y = y

		return
	
def update_squares_from_json() ->list[Square.Square]: 
    """Adds info about each square from the json file to square

    Returns:
        squares (list): List of square
    """
    squares = []

    with open('squareInfo.json', 'r') as file:
        data_dictionary = json.load(file)

    # f = open('squareInfo.json')
    # data_dictionary = json.load(f)
    # f.close()

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

        pygame.draw.rect(screen, (54, 152, 200, 0), (pygame.Rect(square.top_left_x, square.top_left_y, width, height)))
       
    pygame.display.flip()

    return

def find_selected_sprite_from_clicked_square(group: pygame.sprite.RenderPlain, clicked_square: Square.Square):
	"""Finds the selected_sprite using the clicked_square.

	Args:
		group (pygame.sprite.RenderPlain): A group of all the sprites.
		clicked_square (Square.Square): The square that has been clicked

	Returns:
		pygame.sprite: The sprite that is in the clicked square
	"""
	for sprite in group:
		#checking if the centre point falls between the range of x values for the square and same with y.
		if sprite.rect.centerx > clicked_square.top_left_x and sprite.rect.centerx < clicked_square.bottom_right_x:
			if sprite.rect.centery > clicked_square.top_left_y and sprite.rect.centery < clicked_square.bottom_right_y:
				selected_sprite = sprite
				return selected_sprite

def find_clicked_square(clicked_pos_x: int, clicked_pos_y: int, squares: List[Square.Square]) -> Square.Square: 
    """Finds the clicked square object when given coordinates of position.

    Args:
        clicked_pos_x (int): x coordinate of clicked position 
        clicked_pos_y (int): y coordinate of clicked position 
        squares (List[Square.Square]): List of squares

    Returns:
        square (Square): Square
    """
    #TODO: If user clicks outside grid 
    for square in squares:
        if clicked_pos_x > square.top_left_x and clicked_pos_x < square.bottom_right_x and \
        	clicked_pos_y > square.top_left_y and clicked_pos_y < square.bottom_right_y:
            return square

def handle_clicks(self, *args, **kwargs):
	if len(events) > 0:
		if events[0].type == pygame.MOUSEBUTTONUP:
			try:
				global first_clicked_square
			except Exception as e:
				print(e)
			finally:
				global first_clicked_square
				clicked_pos_x, clicked_pos_y = events[0].pos[0], events[0].pos[1]
				print(clicked_pos_x, clicked_pos_y)
				squares = update_squares_from_json()
				clicked_square = find_clicked_square(clicked_pos_x, clicked_pos_y, squares)
			
				# test for whether we're on the first click, and whether the user has clicked on a square with a piece in it			
				if first_clicked_square is None and clicked_square.piece_occupying != "":			
					first_clicked_square = clicked_square
					# find and highlight required squares
					print("first click")
					selected_sprite = find_selected_sprite_from_clicked_square(group, clicked_square)
					valid_moves = helpers.get_valid_moves(selected_sprite)
					return valid_moves
				# test for whether we're on the second click, and whether there's a piece in the square being moved to
				elif first_clicked_square is not None and clicked_square.piece_occupying != "":
					# square to move to is occupied logic
					# TODO Implement taking pieces
					print("Piece in square. Cannot move.")
					print("second click")
				# if on second click and clicked square is unoccupied, 
				elif first_clicked_square is not None and clicked_square.piece_occupying == "":
					# move piece logic
					_ = 1
					print("second click")

					selected_sprite = find_selected_sprite_from_clicked_square(group, first_clicked_square )
					if selected_sprite:
						clicked_square_centre_x = np.mean([clicked_square.top_left_x, clicked_square.bottom_right_x])
						clicked_square_centre_y = np.mean([clicked_square.top_left_y, clicked_square.bottom_right_y])
						on_click(selected_sprite, clicked_square_centre_x, clicked_square_centre_y)
						helpers.update_squareInfojson(first_clicked_square.name, Rank.Rank(selected_sprite.rank).name, clicked_square.name)
						first_clicked_square = None
						selected_sprite = None
						screen.blit(pygame.image.load("chessboard.png"), [0, 0])



def on_click(selected_sprite: pygame.sprite, clicked_square_centre_x, clicked_square_centre_y):
	selected_sprite.movement(clicked_square_centre_x - 30, clicked_square_centre_y - 30)
	
pygame.init()
screen = pygame.display.set_mode((570, 570))
pygame.display.flip()

first_clicked_square = None

group = pygame.sprite.RenderPlain()


def load_graphics(): 
    """defines all pieces as sprites and adds them to group
    Returns:
        group of sprites
    """

	# white
	# pawns
    a2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 26, 428, on_click, "white", 1, 0)
    b2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 97, 428, on_click, "white", 1, 0)
    c2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 165, 428, on_click, "white", 1, 0)
    d2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 224, 428, on_click, "white", 1, 0)
    e2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 295, 428, on_click, "white", 1, 0)
    f2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 358, 428, on_click, "white", 1, 0)
    g2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 430, 428, on_click, "white", 1, 0)
    h2_white_pawn_sprite = ClickableSprite("Pieces\\white\\pawn.png", 489, 428, on_click, "white", 1, 0)    
    
	# rooks
    a1_white_rook_sprite = ClickableSprite("Pieces\\white\\rook.png", 31, 490, on_click, "white", 4, 0)
    h1_white_rook_sprite = ClickableSprite("Pieces\\white\\rook.png", 500, 490, on_click, "white", 4, 0)

	# knights
    b1_white_knight_sprite = ClickableSprite("Pieces\\white\\knight.png", 97, 490, on_click, "white", 2, 0)
    g1_white_knight_sprite = ClickableSprite("Pieces\\white\\knight.png", 430, 490, on_click, "white", 2, 0)

	# bishops
    c1_white_bishop_sprite = ClickableSprite("Pieces\\white\\bishop.png", 165, 490, on_click, "white", 3, 0)
    f1_white_bishop_sprite = ClickableSprite("Pieces\\white\\bishop.png", 358, 490, on_click, "white", 3, 0)

	# king and queen
    d1_white_queen_sprite = ClickableSprite("Pieces\\white\\queen.png", 224, 490, on_click, "white", 5, 0)
    e1_white_king_sprite = ClickableSprite("Pieces\\white\\king.png", 295, 490, on_click, "white", 6, 0)
    
    
	# black
	# pawns
    a7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 26, 87, on_click, "black", 1, 0)
    b7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 97, 87, on_click, "black", 1, 0)
    c7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 165, 87, on_click, "black", 1, 0)
    d7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 224, 87, on_click, "black", 1, 0)
    e7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 295, 87, on_click, "black", 1, 0)
    f7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 358, 87, on_click, "black", 1, 0)
    g7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 430, 87, on_click, "black", 1, 0)
    h7_black_pawn_sprite = ClickableSprite("Pieces\\black\\pawn.png", 489, 87, on_click, "black", 1, 0)
    	
	# rook
    a8_black_rook_sprite = ClickableSprite("Pieces\\black\\rook.png", 31, 17, on_click, "black", 4, 0)
    h8_black_rook_sprite = ClickableSprite("Pieces\\black\\rook.png", 500, 17, on_click, "black", 4, 0)

	# knight
    b8_black_knight_sprite = ClickableSprite("Pieces\\black\\knight.png", 97, 17, on_click, "black", 2, 0)
    g8_black_knight_sprite = ClickableSprite("Pieces\\black\\knight.png", 430, 17, on_click, "black", 2, 0)

	# bishop
    c8_black_bishop_sprite = ClickableSprite("Pieces\\black\\bishop.png", 165, 17, on_click, "black", 3, 0)
    f8_black_bishop_sprite = ClickableSprite("Pieces\\black\\bishop.png", 358, 17, on_click, "black", 3, 0)

	# king & queen
    d8_black_queen_sprite = ClickableSprite("Pieces\\black\\queen.png", 224, 17, on_click, "black", 5, 0)
    e8_black_king_sprite = ClickableSprite("Pieces\\black\\king.png", 290, 17, on_click, "black", 6, 0)
    

	# white
    group.add(a2_white_pawn_sprite, b2_white_pawn_sprite, c2_white_pawn_sprite, d2_white_pawn_sprite, 
        e2_white_pawn_sprite, f2_white_pawn_sprite, g2_white_pawn_sprite, h2_white_pawn_sprite,
		a1_white_rook_sprite, b1_white_knight_sprite, c1_white_bishop_sprite, d1_white_queen_sprite,
		e1_white_king_sprite, f1_white_bishop_sprite, g1_white_knight_sprite, h1_white_rook_sprite) 
       
	# black
    group.add(a7_black_pawn_sprite, b7_black_pawn_sprite, c7_black_pawn_sprite, d7_black_pawn_sprite, 
    	e7_black_pawn_sprite, f7_black_pawn_sprite, g7_black_pawn_sprite, h7_black_pawn_sprite,
	    a8_black_rook_sprite, b8_black_knight_sprite, c8_black_bishop_sprite, d8_black_queen_sprite,
    	e8_black_king_sprite, f8_black_bishop_sprite, g8_black_knight_sprite, h8_black_rook_sprite) 
       
    return group

group = load_graphics()
screen.blit(pygame.image.load("chessboard.png"), [0, 0])


running = True
while running:  
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	vm = handle_clicks(events)
	
	squares_to_highlight = []
	squares = update_squares_from_json()

	if vm is not None:
		for valid_move in vm:
			for square in squares:
				if square.name[0] == valid_move[0] and square.name[1] == valid_move[1]:
					squares_to_highlight.append(square)

		for square in squares_to_highlight:
			pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(square.top_left_x, square.top_left_y, 70, 70)) # always does this and the stuff below

	group.draw(screen)	

	pygame.display.update()

pygame.quit()
