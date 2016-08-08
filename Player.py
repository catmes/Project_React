import pygame
from pygame.locals import *


class Block(pygame.sprite.Sprite):
	# Constructor. Pass in the color of the block,
	# and its x and y position
	def __init__(self, color, width, height, speed):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.speed = speed

		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()


	def move(self, event):
		speed = 6
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.rect.x -= speed
			if event.key == pygame.K_RIGHT:
				self.rect.x += speed
			if event.key == pygame.K_DOWN:
				self.rect.y += speed
			if event.key == pygame.K_UP:
				self.rect.y -= speed











