# All rights is not reserved. Read ./COPYRIGHT

# Utils for tasks 1, 2

from graph import *
import math

C = canvas()

def draw_oval(x, y, a, b)->'int':
	""" (x, y) - center, a - major seim axis, b - minor seim axis """
	# Using tkinter directly
	C.create_oval(x - a, y - b, x + a, y + b,
		outline = penColor(),
		width = penSize(),
		fill = brushColor())
