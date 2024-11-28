import pygame
 
class Button():
	def __init__(self, x, y, image, surface):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.midbottom = (x, y)
		self.clicked = False
		self.surface = surface
		self.clicked = False

	def draw(self):
		self.surface.blit(self.image, (self.rect.x, self.rect.y))
		pos = pygame.mouse.get_pos()
		action = False

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			
		return action




	