#! /usr/bin/env python2

# Here's what we run when we start the game!  It initializes important things such
# as the window settings and it runs the main loop of the game.

from menu import Menu
from grid import Grid
from drop_down import DropDown
import pygame as pg
import sys

FPS = 60

class PixFiz(object):

	def __init__(self):
		pg.init()
		self.set_cursor()
		self.background = self.tile_bg()
		self.screen = pg.display.set_mode((600,400))
		self.clock = pg.time.Clock()
		self.menu = Menu()
		self.grid = Grid()
		self.drop = DropDown()	


	def input(self):
		#key events
		quit = False
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit = True
			elif event.type == pg.MOUSEBUTTONDOWN:
				print "mouse button down"
				print event.pos
				self.grid.mouse_click(event.pos)

		return quit

	def main_loop(self):
		quit = False
		while not quit:
			quit = self.input()

			#draw events
			self.screen.blit(self.background, (0,0))
			self.menu.draw(self.screen)
			self.grid.draw(self.screen)
			self.drop.draw(self.screen)

			#FPS stuff
			pg.display.flip()
			milliseconds = self.clock.tick(FPS)
			pg.display.set_caption("FPS: " + str(self.clock.get_fps()))

	def set_cursor(self):
		pg.mouse.set_cursor(*pg.cursors.arrow)

	def tile_bg(self): #makes the transparent image to use as a bg.
		bg = pg.image.load("back.png")
		trans_back = pg.Surface((600,400))
	
		for i in xrange(0, 600, 32):
			for j in xrange(0, 400, 32):
				trans_back.blit(bg,(i, j))
		return trans_back


if __name__ == "__main__":
	p = PixFiz() #inits
	p.main_loop() #loops
	
