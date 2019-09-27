# All rights is not reserved. Read ./COPYRIGHT

# Draw "cat with threads in room"

from graph import *
import math

from utils import *

width, height = windowSize()
center = width / 2, height / 2

if __name__ == '__main__':
	# Background
	brushColor(mg_clr)
	rectangle(0, 0, width, height*0.45)
	brushColor(mryel_clr)
	rectangle(0, height*0.45, width, height)

	draw_cat(center[0], center[1] + height/8, 170)
	draw_window(center[0] + width*0.28, height*0.23, width*0.4, height*0.4)
	run()
