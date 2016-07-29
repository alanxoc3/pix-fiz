

# Here's the drop down triangle in the corner of the screen.  It has different states,
# based on if we're playing the game, in the main menu, or somewhere else.

import pygame as pg

START = 13

class DropDown(object):

	def __init__(self):
		self.menu_items = ["Pix-Fiz v. 0.10", "Change Username", "Help"]
		self.edit_items = ["Edit Mode", "Pencil", "Fill bucket"]
		self.play_items = ["Back to Edit", "Restart"]
		self.items = self.menu_items

		self.open = False
		self.default_points = [(START,START),(START,START),(START,START*2),(START*2,START)]

		self.x_slide = START
		self.y_slide = START
	
	def draw(self, background): 
		if self.open == True:
			self.x_slide = 60
			self.y_slide = 10*len(self.items) + START
		else:
			self.x_slide = START
			self.y_slide = START

		
		pg.draw.polygon(background, pg.Color("blue"), self.default_points)
			

			

	
