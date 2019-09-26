# All rights is not reserved. Read ./COPYRIGHT

# Utils for tasks 1, 2

from graph import *
import math

# Colors in RGB
op_clr = 250, 150, 100 # Pink with a little orange
grey_clr = 70, 70, 70 # Light-grey
mg_clr = 100, 85, 0 # Marshy green
mryel_clr = 180, 150, 0 # Marshy yellow
pnk_clr = 250, 200, 200 # Pink
gr_clr = 50, 200, 0 # Green with a little yellow
bl_clr = 150, 250, 250 # Light-blue
wh_clr = 255, 255, 255 # White
blk_clr = 0, 0, 0 # Black

C = canvas()

def draw_oval(x, y, a, b)->'int':
	""" (x, y) - center, a - major seim axis, b - minor seim axis """
	# Using tkinter directly
	C.create_oval(x - a, y - b, x + a, y + b,
		outline = penColor(),
		width = penSize(),
		fill = brushColor())
