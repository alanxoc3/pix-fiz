
"""
This is the main menu.  Functionality includes:
  -Displaying a button that says 'host' and 'join'
  -Checking and hosting a game if there is not one available
  -Joining a game if one exists.

-Written by Wadlo
"""

import os
import sys
import pygame as pg


CAPTION = "PixFiz"
SCREEN_SIZE = (600, 400)


class Menu(object):
    def __init__(self):
        self.screen = pg.display
        self.clock = pg.time.Clock()
	self.fps = 60
	self.done = False
	self.keys = pg.key.get_pressed()
	self.color = pg.Color("black")

    def main_loop(self):
        while True:
            for event in pg.event.get():
	        if event.type == pg.QUIT:
		    pg.quit()
                    sys.exit()
    
    def button_click(self):
        pass


def main():
    #Initialize and center screen.

    os.environ['SDL_VIDEO_CENTERED'] = '1' #center the screen...
    pg.init() 
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    Menu().main_loop()
    pg.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()

