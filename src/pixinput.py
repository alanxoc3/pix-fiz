import pygame as pg

m_rel = (0,0)

keys = {
	"MOUSE_MOVED" : False,

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

def update_input():
	keys["LEFT_CLICK_PRESSED"] = False
	keys["LEFT_CLICK_RELEASED"] = False
	keys["RIGHT_CLICK_PRESSED"] = False
	keys["RIGHT_CLICK_RELEASED"] = False

	keys["RIGHT_ARROW_PRESSED"] = False
	keys["RIGHT_ARROW_RELEASED"] = False
	keys["LEFT_ARROW_PRESSED"] = False
	keys["LEFT_ARROW_RELEASED"] = False
	keys["UP_ARROW_PRESSED"] = False
	keys["UP_ARROW_RELEASED"] = False
	keys["DOWN_ARROW_PRESSED"] = False
	keys["DOWN_ARROW_RELEASED"] = False
	keys["QUIT_PRESSED"] = False
	keys["MOUSE_MOVED"] = False

	for event in pg.event.get():
		if event.type == pg.QUIT:
			keys["QUIT_PRESSED"] = True
		elif event.type == pg.MOUSEBUTTONDOWN:
			num = event.button
			if num == 1:
				keys["LEFT_CLICK_PRESSED"] = True
				keys["LEFT_CLICK_DOWN"] = True
			elif num == 3:
				keys["RIGHT_CLICK_PRESSED"] = True
				keys["RIGHT_CLICK_DOWN"] = True
		elif event.type == pg.MOUSEBUTTONUP:
			num = event.button
			if num == 1:
				keys["LEFT_CLICK_RELEASED"] = True
				keys["LEFT_CLICK_DOWN"] = False
			elif num == 3:
				keys["RIGHT_CLICK_RELEASED"] = True
				keys["RIGHT_CLICK_DOWN"] = False
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
				keys["RIGHT_ARROW_PRESSED"] = True
				keys["RIGHT_ARROW_DOWN"] = True
			elif event.key == pg.K_LEFT:
				keys["LEFT_ARROW_PRESSED"] = True
				keys["LEFT_ARROW_DOWN"] = True
			elif event.key == pg.K_UP:
				keys["UP_ARROW_PRESSED"] = True
				keys["UP_ARROW_DOWN"] = True
			elif event.key == pg.K_DOWN:
				keys["DOWN_ARROW_PRESSED"] = True
				keys["DOWN_ARROW_DOWN"] = True
		elif event.type == pg.KEYUP:
			if event.key == pg.K_RIGHT:
				keys["RIGHT_ARROW_RELEASED"] = True
				keys["RIGHT_ARROW_DOWN"] = False
			elif event.key == pg.K_LEFT:
				keys["LEFT_ARROW_RELEASED"] = True
				keys["LEFT_ARROW_DOWN"] = False
			elif event.key == pg.K_UP:
				keys["UP_ARROW_RELEASED"] = True
				keys["UP_ARROW_DOWN"] = False
			elif event.key == pg.K_DOWN:
				keys["DOWN_ARROW_RELEASED"] = True
				keys["DOWN_ARROW_DOWN"] = False
		elif event.type == pg.MOUSEMOTION:
			keys["MOUSE_MOVED"] = True
