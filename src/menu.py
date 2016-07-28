
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


class Menu(object):

	def draw(self, background):
		background.fill(pg.Color("white"), pg.Rect(50,50,50,50))


if __name__ == "__main__":
    main()

