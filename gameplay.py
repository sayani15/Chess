import pygame

class ClickableSprite(pygame.sprite.Sprite):
	def __init__(self, image_file_path, x, y, callback):
		super().__init__()
		#self.image = image
		self.image = pygame.image.load(image_file_path)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.callback = callback
		self.visible = True

	

	def movement(self, x: int, y: int):
		self.rect.x = x
		self.rect.y = y

		return
	
	def update(self, events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONUP:
				for sprite in group:						
					# selected_sprite = None
					if sprite.rect.collidepoint(event.pos):					
						selected_sprite = sprite	
						break
				try:
					selected_sprite 
				except NameError:
					continue
				if selected_sprite != None:					
					clicked_pos_x = event.pos[0]
					clicked_pos_y = event.pos[1]	
					self.callback(selected_sprite, clicked_pos_x, clicked_pos_y)
				



def on_click(selected_sprite, clicked_pos_x, clicked_pos_y):
	selected_sprite.movement(clicked_pos_x, clicked_pos_y)
	# a1_black_rook_sprite.visible = not a1_black_rook_sprite.visible


	
pygame.init()
screen = pygame.display.set_mode((570, 570))

a1_white_rook_sprite = ClickableSprite("Pieces\\white\\rook.png", 31, 490, on_click)

white_bishop = ClickableSprite("Pieces\\white\\bishop.png", 50, 50, on_click)
h1_white_rook_sprite = ClickableSprite("Pieces\\white\\rook.png", 500, 490, on_click)


group = pygame.sprite.RenderPlain(a1_white_rook_sprite, white_bishop, h1_white_rook_sprite)

# group.add(a1_black_rook_sprite)
# group.add(sprite)
# group.add(h1_black_rook_sprite)

running = True
while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			running = False

	group.update(events)
	screen.blit(pygame.image.load("chessboard.png"), [0, 0])
	if white_bishop.visible:
		group.draw(screen)
	pygame.display.update()

pygame.quit()
