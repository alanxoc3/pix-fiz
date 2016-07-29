

class Input:
	keys = {
		"LEFT_CLICK_DOWN" : False,
		"LEFT_CLICK_PRESSED" : False,
		"LEFT_CLICK_RELEASED" : False,

		"RIGHT_CLICK_DOWN" : False,
		"RIGHT_CLICK_PRESSED" : False,
		"RIGHT_CLICK_RELEASED" : False,

		"RIGHT_ARROW_DOWN" : False,
		"RIGHT_ARROW_PRESSED" : False,
		"RIGHT_ARROW_RELEASED" : False,

		"LEFT_ARROW_DOWN" : False,
		"LEFT_ARROW_PRESSED" : False,
		"LEFT_ARROW_RELEASED" : False,

		"UP_ARROW_DOWN" : False,
		"UP_ARROW_PRESSED" : False,
		"UP_ARROW_RELEASED" : False,

		"DOWN_ARROW_DOWN" : False,
		"DOWN_ARROW_PRESSED" : False,
		"DOWN_ARROW_RELEASED" : False,

		"QUIT_PRESSED" : False
	}

	@classmethod
	def update_input(cls):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit = True
			elif event.type == pg.MOUSEBUTTONDOWN:
				print "mouse left down", event.pos
				cls.keys
			elif event.type == pg.MOUSEBUTTONDOWN:
				print "mouse button down"
				print event.pos
				self.grid.mouse_click(event.pos)
		
		"LEFT_CLICK_DOWN" : False,
		"LEFT_CLICK_PRESSED" : False,
		"LEFT_CLICK_RELEASED" : False,

		"RIGHT_CLICK_DOWN" : False,
		"RIGHT_CLICK_PRESSED" : False,
		"RIGHT_CLICK_RELEASED" : False,

