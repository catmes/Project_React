import pygame
import os
from Player import Player
from enemy import Enemy
from pygame.locals import *

# just setting some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# setting up local dir and image dir
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

# game objects
clock = pygame.time.Clock()
player = Player(WHITE, 50, 50)
enemy = Enemy()
all_sprites = pygame.sprite.RenderPlain(player, enemy)

# player starting pos
player.rect.x = screen.get_width() / 2 - player.rect.width / 2
player.rect.y = screen.get_width() / 2 - player.rect.height / 2

going = True
# main game loop
while going:
	clock.tick(60)
	# event handling
	for event in pygame.event.get():
		if event.type == QUIT:
			going = False
		# controller input
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.dx.insert(0, -player.speed)
			elif event.key == pygame.K_RIGHT:
				player.dx.insert(0, player.speed)
			elif event.key == pygame.K_DOWN:
				player.dy.insert(0, player.speed)
			elif event.key == pygame.K_UP:
				player.dy.insert(0, -player.speed)
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.dx.remove(-player.speed)
			elif event.key == pygame.K_RIGHT:
				player.dx.remove(player.speed)
			elif event.key == pygame.K_DOWN:
				player.dy.remove(player.speed)
			elif event.key == pygame.K_UP:
				player.dy.remove(-player.speed)

	# updating display
	player.update()
	player.collision()
	screen.blit(background, (0, 0))
	all_sprites.draw(screen)
	pygame.display.flip()

print main_dir
pygame.quit()



