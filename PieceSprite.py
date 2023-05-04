import pygame as pg

class PieceSprite(pg.sprite.Sprite):
    def __init__(self, position):
        super(PieceSprite, self).__init__()
        self.image = pg.image.load("Pieces\\black\\pawn.png")
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        pass

    
        