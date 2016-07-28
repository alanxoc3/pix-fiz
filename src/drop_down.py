

# Here's the drop down triangle in the corner of the screen.  It has different states,
# based on if we're playing the game, in the main menu, or somewhere else.

import pygame as pg

class DropDown(object):

	def __init__(self):
		self.menu_items = ["Pix-Fiz v. 0.10", "Change Username", "Help"]
		self.edit_items = ["Edit Mode", "Pencil", "Fill bucket"]
		self.play_items = ["Back to Edit", "Restart"]

		self.open = False

		self.x_slide = 0
		self.y_slide = 0
	
	def draw(self, background): 
		if self.open == True:
			pass
		else:
			pg.draw.polygon(background, pg.Color("blue")
			
			

	
