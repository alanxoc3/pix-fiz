# Following a tutorial
import pygame
import sys
from enum import Enum

FPS = 60
DIM = (600,400)

class Dir(Enum):
	#up, down, left, right = (0, 1, 2, 3)
	up = 0
	down = 1
	left = 2
	right = 3

class KeyState(Enum):
	#up, down, left, right = (0, 1, 2, 3)
	none = 0
	released = 1
	pressed = 2

class SpamBot:
	"""
	Just a test to see how an object can be used to draw.
	"""
	def __init__(self, screen, pathname):
		self.x, self.y = screen.get_size()
		self.pic = pygame.image.load(pathname)

	def display(self, screen):
		screen.blit(self.pic, (self.x, self.y))

	def input(self, arrows):
		if arrows[Dir.up]:
			y -= 1
		if arrows[Dir.down]:
		 	y += 1
		if arrows[Dir.left]:
		 	x -= 1
		if arrows[Dir.right]:
			x += 1

def main():
	pygame.init()

	screen = pygame.display.set_mode(DIM)
	spammy = SpamBot(screen, "Spambot.png")

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
		screen.blit(background, (0, 0))

		spammy.display(screen)

		#screen.fill((255, 255, 255))
		#pygame.draw.line(screen, (100, 150, 200), (0,0), (100,100), 10)
		pygame.display.flip()
		milliseconds = clock.tick(FPS)
		pygame.display.set_caption("FPS: " + str(clock.get_fps()))

if __name__ == "__main__":
	main()
