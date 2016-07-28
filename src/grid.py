import pygame as pg

class Grid(object):
	def __init__(self):
		self.res = (600,400) # The dimension of the surface
		self.pix = (6,4) # Number of pixels on screen/board/canvas
		self.xoffset, self.yoffset = 0, 0 # Offset on surface that things are drawn.
		self.grid = pg.Surface(self.res)
		self.zoom_factor = 1.0

		# Creating the matrix
		self.pix_dim = (self.res[0] / self.pix[0], self.res[1] / self.pix[1])
		self.pix_matrix = [[0 for x in range(self.pix[0])] for y in range(self.pix[1])] 

		# Initialize the matrix now.
		for row in range(0,self.pix[1]):
			for col in range(0,self.pix[0]):
				self.pix_matrix[row][col] = 0

		self.pix_matrix[1][0] = 1 # Testing

		# Drawing stuff
		self.draw_onto_surface()

	def mouse_click(self, pos, offset=(0,0)):
		x = (pos[0] + offset[0]) / self.pix_dim[0]
		y = (pos[1] + offset[1]) / self.pix_dim[1]
		self.pix_matrix[y][x] = 1
		self.draw_onto_surface()

	def zoom_in(self, pos, amount=1):
		
		pass

	def zoom_out(self, pos, amount=1):
		pass

	def draw_onto_surface(self):
		self.key = (249, 17, 17) # The Color Key
		self.grid.fill(self.key)
		self.grid.set_colorkey(self.key)
		self.grid.set_alpha(255)
		self.drawRects()
		self.drawLines() # Draws the lines onto the surface.

	def drawRects(self):
		colors = ((0,0,0,255)) # One color right now, green
		for row in range(0,self.pix[1]):
			for col in range(0,self.pix[0]):
				val = self.pix_matrix[row][col]
				if val == 1:
					pos = (col * self.pix_dim[0] + self.xoffset, row * self.pix_dim[1] + self.yoffset)
					r = pg.Rect(pos, self.pix_dim)
					#pg.draw.rect(self.grid, colors[0], r)
					self.grid.fill(colors[0], r)
		
	def drawLines(self):
		print self.grid.get_alpha()
		color = (0,0,0,240)
		width = 1

		for y in xrange(0, self.res[1] + 1, self.pix_dim[1]): # Horizontal lines
			tup1 = (0 + self.xoffset          , y + self.yoffset)
			tup2 = (self.res[0] + self.xoffset, y + self.yoffset)
			pg.draw.line(self.grid, color, tup1, tup2, width)

		for x in xrange(0, self.res[0] + 1, self.pix_dim[0]): # Vertical lines
			tup1 = (x + self.xoffset, 0 + self.yoffset          )
			tup2 = (x + self.xoffset, self.res[1] + self.yoffset)
			pg.draw.line(self.grid, color, tup1, tup2, width)

	def draw(self, screen):
		screen.blit(self.grid, (0,0))
