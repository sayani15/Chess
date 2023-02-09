import pygame
from win32api import GetSystemMetrics

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

def starting_positions(screen, graphics):
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









graphics = load_graphics()

background_colour = (0, 150, 250)
#(width, height) = (0.9*GetSystemMetrics(0), 0.9*GetSystemMetrics(1))
(width, height) = (600, 600)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("chess")
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    screen.blit(board, [0, 0])
    starting_positions(screen, graphics)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked_position = pygame.mouse.get_pos()
            print(clicked_position)
