import rank as Rank
import pygame


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