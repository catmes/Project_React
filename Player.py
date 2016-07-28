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

	# Returns what key is pressed.
	def check_key(self, event_list):
		for my_event in event_list:
			if my_event.type == pygame.KEYDOWN:
				return my_event.key

	def move(self, event_list):

		key_pressed = self.check_key(event_list)
		key_held = pygame.key.get_pressed()

		if key_held[K_RIGHT] == True:
			self.rect.x += self.speed
		if key_held[K_LEFT] == True:
			self.rect.x -= self.speed
		if key_held[K_DOWN] == True:
			self.rect.y += self.speed
		if key_held[K_UP] == True:
			self.rect.y -= self.speed




