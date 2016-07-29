import pygame as pg

m_rel = (0,0)

keys = {
	"MOUSE_MOVED" : False,
	"WHEEL_UP" : False,
	"WHEEL_DOWN" : False,

	"LEFT_CLICK" : False,
	"LEFT_CLICK_PRESSED" : False,
	"LEFT_CLICK_RELEASED" : False,
	"LEFT_CLICK_ALT" : False,

	"MIDDLE_CLICK" : False,
	"MIDDLE_CLICK_PRESSED" : False,
	"MIDDLE_CLICK_RELEASED" : False,

	"RIGHT_CLICK" : False,
	"RIGHT_CLICK_PRESSED" : False,
	"RIGHT_CLICK_RELEASED" : False,
	"RIGHT_CLICK_ALT" : False,

	"RIGHT_ARROW" : False,
	"RIGHT_ARROW_PRESSED" : False,
	"RIGHT_ARROW_RELEASED" : False,

	"LEFT_ARROW" : False,
	"LEFT_ARROW_PRESSED" : False,
	"LEFT_ARROW_RELEASED" : False,

	"UP_ARROW" : False,
	"UP_ARROW_PRESSED" : False,
	"UP_ARROW_RELEASED" : False,

	"DOWN_ARROW" : False,
	"DOWN_ARROW_PRESSED" : False,
	"DOWN_ARROW_RELEASED" : False,

	"ESCAPE" : False,
	"QUIT" : False
}

def update_input():
	# RESET KEYS
	keys["LEFT_CLICK_PRESSED"] = False
	keys["LEFT_CLICK_RELEASED"] = False
	keys["RIGHT_CLICK_PRESSED"] = False
	keys["RIGHT_CLICK_RELEASED"] = False
	keys["WHEEL_UP"] = False
	keys["WHEEL_DOWN"] = False

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
	keys["ESCAPE"] = False
	keys["MIDDLE_CLICK_PRESSED"] = False
	keys["MIDDLE_CLICK_RELEASED"] = False

	for event in pg.event.get():
		if event.type == pg.QUIT:
			keys["QUIT_PRESSED"] = True
		elif event.type == pg.MOUSEBUTTONDOWN:
			num = event.button
			if num == 1:
				if pg.key.get_mods() & pg.KMOD_ALT:
					keys["LEFT_CLICK_ALT"] = True
				else:
					keys["LEFT_CLICK_PRESSED"] = True
					keys["LEFT_CLICK"] = True
			elif num == 2:
				keys["MIDDLE_CLICK_PRESSED"] = True
				keys["MIDDLE_CLICK"] = True
			elif num == 3:
				if pg.key.get_mods() & pg.KMOD_ALT:
					keys["RIGHT_CLICK_ALT"] = True
				else:
					keys["RIGHT_CLICK_PRESSED"] = True
					keys["RIGHT_CLICK"] = True
			elif num == 4:
				keys["WHEEL_UP"] = True
			elif num == 5:
				keys["WHEEL_DOWN"] = True
		elif event.type == pg.MOUSEBUTTONUP:
			num = event.button
			if num == 1:
				keys["LEFT_CLICK_RELEASED"] = True
				keys["LEFT_CLICK"] = False
				keys["LEFT_CLICK_ALT"] = False
			elif num == 2:
				keys["MIDDLE_CLICK_RELEASED"] = True
				keys["MIDDLE_CLICK"] = False
			elif num == 3:
				keys["RIGHT_CLICK_RELEASED"] = True
				keys["RIGHT_CLICK"] = False
				keys["RIGHT_CLICK_ALT"] = False
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
				keys["RIGHT_ARROW_PRESSED"] = True
				keys["RIGHT_ARROW"] = True
			elif event.key == pg.K_LEFT:
				keys["LEFT_ARROW_PRESSED"] = True
				keys["LEFT_ARROW"] = True
			elif event.key == pg.K_UP:
				keys["UP_ARROW_PRESSED"] = True
				keys["UP_ARROW"] = True
			elif event.key == pg.K_DOWN:
				keys["DOWN_ARROW_PRESSED"] = True
				keys["DOWN_ARROW"] = True
			elif event.key == pg.K_ESCAPE:
				keys["ESCAPE"] = True
		elif event.type == pg.KEYUP:
			if event.key == pg.K_RIGHT:
				keys["RIGHT_ARROW_RELEASED"] = True
				keys["RIGHT_ARROW"] = False
			elif event.key == pg.K_LEFT:
				keys["LEFT_ARROW_RELEASED"] = True
				keys["LEFT_ARROW"] = False
			elif event.key == pg.K_UP:
				keys["UP_ARROW_RELEASED"] = True
				keys["UP_ARROW"] = False
			elif event.key == pg.K_DOWN:
				keys["DOWN_ARROW_RELEASED"] = True
				keys["DOWN_ARROW"] = False
		elif event.type == pg.MOUSEMOTION:
			keys["MOUSE_MOVED"] = True

	if keys["MOUSE_MOVED"] == True:
		global m_rel
		m_rel = pg.mouse.get_rel()

