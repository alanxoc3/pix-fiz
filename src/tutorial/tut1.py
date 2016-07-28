#! /usr/bin/env python2

# Following a tutorial
import pygame
import sys

FPS = 60
DIM = (600,400)

class Dir(object):
	#up, down, left, right = (0, 1, 2, 3)
	up = 0
	down = 1
	left = 2
	right = 3

class KeyState(object):
	#up, down, left, right = (0, 1, 2, 3)
	none = 0
	released = 1
	pressed = 2

class Square(pygame.sprite.Sprite):
	"""
	A pixel!
	"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface((64, 64))
		self.image.fill((12, 89, 200))
		self.rect = self.image.get_rect()

class SpamBot(pygame.sprite.Sprite):
	"""
	Just a test to see how an object can be used to draw.
	"""
	def __init__(self, screen, pathname):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(pathname)
		self.rect = self.image.get_rect()

		dims = screen.get_size()
		img_dims = self.image.get_size()

		self.rect.x = dims[0] / 2 - img_dims[0] / 2
		self.rect.y = dims[1] / 2 - img_dims[1] / 2

	def input(self, arrows):
		if arrows[Dir.up]:
			self.rect.y -= 1
		if arrows[Dir.down]:
		 	self.rect.y += 1
		if arrows[Dir.left]:
		 	self.rect.x -= 1
		if arrows[Dir.right]:
			self.rect.x += 1

def main():
	pygame.init()

	screen = pygame.display.set_mode(DIM)
	spammy = SpamBot(screen, "Spambot.png")
	sprites = pygame.sprite.LayeredUpdates()
	sprites.add(spammy)
	sprites.add(Square())

	background = pygame.Surface(screen.get_size())
	pygame.draw.line(background, (100, 150, 200), (250,250), (300,250), 5)
	pygame.draw.line(background, (100, 150, 200), (0,0), (100,100), 10)
	#background.fill((255,255,255))
	#background = background.convert()
	clock = pygame.time.Clock()

	arrowHeld = [False, False, False, False]
	mainloop = True
	while mainloop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					mainloop = False
					#pygame.display.toggle_fullscreen()
				elif event.key == pygame.K_UP:
					arrowHeld[0] = True
				elif event.key == pygame.K_DOWN:
					arrowHeld[1] = True
				elif event.key == pygame.K_LEFT:
					arrowHeld[2] = True
				elif event.key == pygame.K_RIGHT:
					arrowHeld[3] = True
				elif event.key == pygame.K_SPACE:
					inc = 30
					for sprite in sprites:
						sprites.change_layer(sprite, inc)
						inc -= 1
						
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					arrowHeld[0] = False
				elif event.key == pygame.K_DOWN:
					arrowHeld[1] = False
				elif event.key == pygame.K_LEFT:
					arrowHeld[2] = False
				elif event.key == pygame.K_RIGHT:
					arrowHeld[3] = False

		spammy.input(arrowHeld)

		# Draw a line
		background.fill((255, 255, 255))
		sprites.draw(background)
		screen.blit(background, (0, 0))

		#pygame.draw.line(screen, (100, 150, 200), (0,0), (100,100), 10)
		pygame.display.flip()
		milliseconds = clock.tick(FPS)
		pygame.display.set_caption("FPS: " + str(clock.get_fps()))

if __name__ == "__main__":
	main()
