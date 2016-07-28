# Following a tutorial
import pygame
import sys

FPS = 60

class SpamBot:
	def __init__(self):
		print "init is not cool."

	def tryAMethod(self):
		print "Plates are cool."

def main():
	SpamBot().tryAMethod()
	pygame.init()
	spammy = pygame.image.load("Spambot.png")
	x = 50
	y = 50

	screen = pygame.display.set_mode((640,480))
	background = pygame.Surface(screen.get_size())
	pygame.draw.line(background, (100, 150, 200), (250,250), (300,250), 5)
	pygame.draw.line(background, (100, 150, 200), (0,0), (100,100), 10)
	#background.fill((255,255,255))
	#background = background.convert()
	clock = pygame.time.Clock()

	arrowHeld = (False, False, False, False)
	mainloop = True
	while mainloop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.display.toggle_fullscreen()
				elif event.key == pygame.K_UP:
					arrowHeld[0] = True
				elif event.key == pygame.K_DOWN:
					arrowHeld[1] = True
				elif event.key == pygame.K_LEFT:
					arrowHeld[2] = True
				elif event.key == pygame.K_RIGHT:
					arrowHeld[3] = True

		if arrowHeld[0]
			y -= 1
		elif arrowHeld[1]
			y += 1
		elif arrowHeld[2]
			x -= 1
		elif arrowHeld[3]
			x += 1
		# Draw a line
		screen.blit(background, (0, 0))

		try:
			spammy
		except NameError:
			pass
		else:
			screen.blit(spammy, (x, y))

		#screen.fill((255, 255, 255))
		#pygame.draw.line(screen, (100, 150, 200), (0,0), (100,100), 10)
		pygame.display.flip()
		milliseconds = clock.tick(FPS)
		pygame.display.set_caption("FPS: " + str(clock.get_fps()))

if __name__ == "__main__":
	main()
