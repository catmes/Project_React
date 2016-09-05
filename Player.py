import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.speed = 4
		self.dx = []
		self.dy = []
		self.rect = self.image.get_rect()

	def update(self):
		try:
			self.rect.x += self.dx[0]  # Index error if the list is empty.
		except IndexError:
			self.rect.x += 0
		try:
			self.rect.y += self.dy[0]  # Index error if the list is empty.
		except IndexError:
			self.rect.y += 0

	def collision(self):
		screen = pygame.display.get_surface()
		# right side
		if self.rect.x > screen.get_width() - self.image.get_width():
			self.rect.x -= self.dx[0]
		# left side
		if self.rect.x < 0:
			self.rect.x -= self.dx[0]
		# bottom side
		if self.rect.y > screen.get_height() - self.image.get_height():
			self.rect.y -= self.dy[0]
		# top side
		if self.rect.y < 0:
			self.rect.y -= self.dy[0]















