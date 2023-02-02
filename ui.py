import pygame
from win32api import GetSystemMetrics

bg = pygame.image.load("chessboard.png")

def load_graphics():
    result = {}
    result["black_pawn"] = pygame.image.load("Pieces\\black\\pawn.png")

    return result

graphics = load_graphics()

background_colour = (0, 150, 250)
(width, height) = (0.9*GetSystemMetrics(0), 0.9*GetSystemMetrics(1))
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("chess")
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    screen.blit(bg, [0, 0])
    screen.blit(graphics["black_pawn"], [0, 0])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

