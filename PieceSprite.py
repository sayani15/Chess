import pygame as pg

class PieceSprite(pg.sprite.Sprite):
    def __init__(self, position, image_file_path):
        super(PieceSprite, self).__init__()
        self.image = pg.image.load(image_file_path)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self):
        pass

    
        