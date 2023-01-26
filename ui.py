import pygame

bg = pygame.image.load("bg.png")


background_colour = (0, 255, 0)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")
screen.fill(background_colour)
pygame.display.flip()
running = True
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False