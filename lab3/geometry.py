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

def draw_polygon_by_angles(x, y, R:'[float]',
	angles:'[float]')->'int':
	""" (x, y) - center,
	R - list of radiuses, R[n] is distance between n-th vertex and center
	angles - list of angles,
	angles[n] is radian angle between horizontal and n-th vertex from center,
	returns link to polygon"""
	vertexes = []
	for n in range(len(angles)):
		vertexes.append((x + math.cos(angles[n])*R[n], y - math.sin(angles[n])*R[n]))
	return polygon(vertexes)

def draw_curve(x, y, R, a, stinc, precision:'int' = 1000)->'int':
	""" (x, y)- center, R - curvage radius, a - angle of sector,
	precision - count of points on circle,
	returns link to polyline """
	points = []
	count_of_points = int(abs(2*math.pi/a) * precision)
	d_angle = a / count_of_points
	d = abs(d_angle) * R
	for i in range(count_of_points):
		points.append((x, y))
		angle = stinc + i * d_angle
		x += d * math.cos(angle)
		y -= d * math.sin(angle)
	return polyline(points)

def draw_thread(x, y, size, angle, precision = 100, periods:'float' = 2.3):
	points = []
	count_of_points = int(size * precision)
	d = size / count_of_points
	X = 0
	Y = 0
	s = math.sin(angle)
	c = math.cos(angle)
	for i in range(count_of_points):
		Y = math.sin(X/size * math.pi * 2 * periods) * size / 20
		points.append((x + X*c - Y*s, y - X*s - Y*c))
		X += d
	return polyline(points)
