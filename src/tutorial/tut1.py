# Following a tutorial
import pygame
import sys

FPS = 60

def main():
	pygame.init()
	spammy = pygame.image.load("Spambot.png")

	screen = pygame.display.set_mode((640,480))
	background = pygame.Surface(screen.get_size())
	pygame.draw.line(background, (100, 150, 200), (250,250), (300,250), 5)
	pygame.draw.line(background, (100, 150, 200), (0,0), (100,100), 10)
	#background.fill((255,255,255))
	#background = background.convert()
	clock = pygame.time.Clock()

	mainloop = True
	while mainloop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.display.toggle_fullscreen()

		# Draw a line
		screen.blit(background, (0, 0))
		screen.blit(spammy, (30, 40))
		#screen.fill((255, 255, 255))
		#pygame.draw.line(screen, (100, 150, 200), (0,0), (100,100), 10)
		pygame.display.flip()
		milliseconds = clock.tick(FPS)
		pygame.display.set_caption("FPS: " + str(clock.get_fps()))

if __name__ == "__main__":
	main()
