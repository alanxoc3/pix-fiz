

# Here's the drop down triangle in the corner of the screen.  It has different states,
# based on if we're playing the game, in the main menu, or somewhere else.

import pygame as pg

START = 14

class DropDown(object):

	def __init__(self):
		self.menu_items = ["Pix-Fiz v. 0.10", "Change Username", "Help"]
		self.edit_items = ["Edit Mode", "Pencil", "Fill bucket"]
		self.play_items = ["Back to Edit", "Restart"]
		self.items = self.menu_items

		self.open = False
		self.default_points = [(START/2,START/2),(START/2,START/2),(START/2,START/2),(START*2,START/2),(START/2,START*2)]


		self.x_slide = START/2
		self.y_slide = START/2
	
	def draw(self, background): 
		if self.open == True:
			self.x_slide = 200
			self.y_slide = 80*len(self.items) + START
		else:
			self.x_slide = START/2
			self.y_slide = START/2

		
		#Animation stuff
		x, y = self.default_points[0]
		x2, y2 = self.default_points[2]

		x2 = (x2+self.x_slide)/2
		y = (y+self.y_slide)/2
		
		self.default_points[0] = x,y
		self.default_points[2] = x2, y2
		self.default_points[1] = x2, y
		
		pg.draw.polygon(background, pg.Color("blue"), self.default_points)
			

	def clicked_on(self):
		if self.open == True:
			self.open = False
		else:
			self.open = True
			

	
