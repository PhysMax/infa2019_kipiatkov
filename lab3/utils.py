# All rights is not reserved. Read ./COPYRIGHT

# Utils for tasks 1, 2

import math
from graph import *

from geometry import *

# Colors in RGB
op_clr = 255, 155, 90 # Pink with a little orange
grey_clr = 70, 70, 70 # Light-grey
mg_clr = 100, 85, 0 # Marshy green
mryel_clr = 180, 150, 0 # Marshy yellow
pnk_clr = 250, 200, 200 # Pink
gr_clr = 140, 200, 0 # Green with a little yellow
bl_clr = 150, 250, 250 # Light-blue
wh_clr = 255, 255, 255 # White
blk_clr = 0, 0, 0 # Black

def draw_head_of_cat(x, y, size):
	penColor(grey_clr)
	brushColor(op_clr)

	draw_oval(x, y, size, size*7/8)

	# Left eye
	brushColor(gr_clr)
	draw_oval(x - size*0.4, y + size/10, size/4, size*0.28)
	brushColor(blk_clr)
	penColor(blk_clr)
	draw_oval(x - size*0.4 + size/12, y + size/10, size/30, size*0.25)

	# Right eye
	brushColor(gr_clr)
	draw_oval(x + size*0.4, y + size/10, size/4, size*0.28)
	brushColor(blk_clr)
	penColor(blk_clr)
	draw_oval(x + size*0.4 + size/12, y + size/10, size/30, size*0.25)

def draw_cat(x, y, size):
	penColor(grey_clr)
	brushColor(op_clr)

	# Body
	draw_oval(x, y, size, size/2)

	# Fore left paw
	draw_oval(x - size*2/3, y + size*5/12, size/4, size/8)

	# Fore right paw
	draw_oval(x - size, y, size/7, size/3)

	# Back left paw
	draw_oval(x + size*2/3, y + size/4, size/3, size/3)
	draw_oval(x + size*0.97, y + size*2/3*0.9, size/10, size/4)

	# Head
	draw_head_of_cat(x - size*0.9, y - size/7, size*0.4)
