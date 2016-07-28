import pygame as pg

class Canvas(pg.Rect):
	def __init__(self, resolution):
		self.grid = pg.Surface(resolution)
		self.grid.fill((100, 10, 255))

	def drawLines(self):
		print self.grid.get_alpha()

	def draw(self, screen):
		screen.blit(self.grid, (100, 100))
