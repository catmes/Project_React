import pygame
import os


class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join("images/triangle.png"))
		self.image.convert()
		self.rect = self.image.get_rect()





