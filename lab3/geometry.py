# All rights is not reserved. Read ./COPYRIGHT

# Functions for drawing some geometry figures

import math
from graph import *

C = canvas()

def draw_rect(startX:'float', startY:'float',
		width:'float', height:'float',
		angle:'float'=0)->'int':
	""" Draw rectangle width * height starting from (startX, startY)
	with rotated to angle (in radians).
	Return link to rectangle. """
	s = math.sin(angle)
	c = math.cos(angle)
	return polygon([(startX, startY),
	(startX + width * c, startY - width * s),
	(startX + width * c + height * s, startY - width * s + height * c),
	(startX + height * s, startY + height * c)])

def draw_oval(x, y, a, b)->'int':
	""" (x, y) - center, a - major seim axis, b - minor seim axis, returns link to oval """
	# Using tkinter directly
	return C.create_oval(x - a, y - b, x + a, y + b,
		outline = penColor(),
		width = penSize(),
		fill = brushColor())

def draw_polygon_by_angles(x, y, R,
	angles:'[float]')->'int':
	""" (x, y) - center,
	R - radius of circumscribed circle,
	angles - list of angles,
	angles[n] is radian angle between vertical and n-th vertex from center,
	returns link to polygon"""
	vertexes = []
	for a in angles:
		vertexes.append((x + math.cos(a)*R, y + math.sin(a)*R))
	return polygon(vertexes)
