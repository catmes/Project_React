import pygame
import os
from Player import Block
from pygame.locals import *

WHITE = (255, 255, 255)

main_dir = os.path.split(os.path.abspath(__file__))[0]
images_dir = os.path.join(main_dir, 'images')

# starting pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('project_game')
pygame.mouse.set_visible(1)

# setting icon
me = os.path.join(images_dir, 'smirk.JPG')
me = pygame.image.load(me)
pygame.display.set_icon(me)

# background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 250, 250))

# display background
screen.blit(background, (0, 0))
pygame.display.flip()

# game objects
clock = pygame.time.Clock()
player = Block(WHITE, 50, 50, 3)
all_sprites = pygame.sprite.RenderPlain(player)

going = True
# main game loop
while going:
	clock.tick(60)

	# event handling
	for event in pygame.event.get():
		if event.type == QUIT:
			going = False

	#controller input
	player.move(pygame.event.get())

	#updating display
	screen.blit(background, (0, 0))
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()



