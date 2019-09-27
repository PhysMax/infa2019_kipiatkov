# All rights is not reserved. Read ./COPYRIGHT

# Utils for tasks 1, 2

import math
from graph import *

from geometry import *

# Colors in RGB
op_clr = 255, 155, 90 # Pink with a little orange
grey_clr = 100, 100, 100 # Light-grey
mg_clr = 100, 85, 0 # Marshy green
mryel_clr = 150, 120, 0 # Marshy yellow
pnk_clr = 250, 200, 200 # Pink
gr_clr = 140, 200, 0 # Green with a little yellow
bl_clr = 100, 200, 200 # Light-blue
wh_clr = 255, 255, 255 # White
blk_clr = 0, 0, 0 # Black
lgr_clr = 180, 180, 180 # Light-light-grey

def draw_head_of_cat(x, y, size, clr):
    penColor(grey_clr)
    brushColor(clr)

    draw_oval(x, y, size, size * 7 / 8)

    # Left eye
    brushColor(gr_clr)
    draw_oval(x - size * 0.4, y + size / 10, size / 4, size * 0.28)
    brushColor(blk_clr)
    penColor(blk_clr)
    draw_oval(x - size * 0.4 + size / 12, y + size / 10, size / 30, size * 0.25)

    # Right eye
    brushColor(gr_clr)
    draw_oval(x + size * 0.4, y + size / 10, size / 4, size * 0.28)
    brushColor(blk_clr)
    penColor(blk_clr)
    draw_oval(x + size * 0.4 + size / 12, y + size / 10, size / 30, size * 0.25)
    brushColor(wh_clr)
    penColor(wh_clr)

    penColor(grey_clr)

    # Right ear
    brushColor(clr)
    draw_polygon_by_angles(x + size * 0.7, y - size * 0.7,
                           [size / 2, size / 3, size / 3], [math.pi / 3, -math.pi / 3, -math.pi])
    brushColor(pnk_clr)
    draw_polygon_by_angles(x + size * 0.7, y - size * 0.7,
                           [size / 3, size * 2 / 9, size * 2 / 9], [math.pi / 3, -math.pi / 3, -math.pi])

    # Left ear
    brushColor(clr)
    draw_polygon_by_angles(x - size * 0.7, y - size * 0.7,
                           [size / 2, size / 3, size / 3], [math.pi * 2 / 3, -math.pi * 2 / 3, 0])
    brushColor(pnk_clr)
    draw_polygon_by_angles(x - size * 0.7, y - size * 0.7,
                           [size / 3, size * 2 / 9, size * 2 / 9], [math.pi * 2 / 3, -math.pi * 2 / 3, 0])

    # Nose
    draw_polygon_by_angles(x, y + size / 2,
                           [size / 10, size / 15, size / 10], [math.pi / 6, -math.pi / 2, -math.pi * 7 / 6])
    line(x, y + size / 2 + size / 15, x, y + size * 2 / 3)

    # Mouth
    draw_curve(x, y + size * 2 / 3, size / 10, math.pi / 2, -math.pi / 6)
    draw_curve(x, y + size * 2 / 3, size / 10, -math.pi / 2, -math.pi * 5 / 6)

    # Mustache
    draw_curve(x + size / 5, y + size * 0.55, size * 4, -math.pi / 8, math.pi * 0.125)
    draw_curve(x + size / 5, y + size * 0.60, size * 4, -math.pi / 8, math.pi * 0.1)
    draw_curve(x + size / 5, y + size * 0.65, size * 4, -math.pi / 8, math.pi * 0.075)
    draw_curve(x - size / 5, y + size * 0.55, size * 4, math.pi / 8, math.pi * 0.875)
    draw_curve(x - size / 5, y + size * 0.60, size * 4, math.pi / 8, math.pi * 0.9)
    draw_curve(x - size / 5, y + size * 0.65, size * 4, math.pi / 8, math.pi * 0.925)

def draw_cat(x, y, sizeX, sizeY, clr):
    """ sizeX - some horizontal scale of the cat, sizeY some vertical scale,
    to mirror cat you should take sizeX < 0,
    to draw "standart" cat use same values of sizeX and sizeY
    clr - color of cat"""
    penColor(grey_clr)
    brushColor(clr)

    # Tail
    if sizeX * sizeY < 0:  # Cat is mirrored
        angle = -math.pi * 5 / 6
    else:
        angle = -math.pi / 6
    a = sizeX / math.cos(angle)
    b = sizeY / (3 * math.cos(angle))
    draw_rect(x + sizeX, y, a, b, angle)

    # Body
    draw_oval(x, y, sizeX, sizeY / 2)

    # Fore left paw
    draw_oval(x - sizeX * 2 / 3, y + sizeY * 5 / 12, sizeX / 4, sizeY / 8)

    # Fore right paw
    draw_oval(x - sizeX, y, sizeX / 7, sizeY / 3)

    # Back left paw
    draw_oval(x + sizeX * 2 / 3, y + sizeY / 4, sizeX / 3, sizeY / 3)
    draw_oval(x + sizeX * 0.97, y + sizeY * 2 / 3 * 0.9, sizeX / 10, sizeY / 4)

    # Head
    draw_head_of_cat(x - sizeX * 0.9, y - sizeY / 7, sizeY * 0.4, clr)

def draw_window(x, y, width, height, indentX = None, indentY = None):
	""" (x, y) - center , (width, height) - size,
	indentX - horizontal indent between "glasses"
	indentY - vertical indent between "glasses" """
	if indentX == None:
		indentX = width*0.05
	if indentY == None:
		indentY = height*0.05

	brushColor(wh_clr)
	penColor(wh_clr)
	rectangle(x - width/2, y - height/2, x + width/2, y + height/2)

	brushColor(bl_clr)
	rectangle(x - width/2 + indentX, y - height/2 + indentY, x - indentX/2, y - indentY/2 - height/6)
	rectangle(x + indentX/2, y - height/2 + indentY, x + width/2 - indentX, y - indentY/2 - height/6)
	rectangle(x - width/2 + indentX, y + indentY/2 - height/6, x - indentX/2, y + height/2 - indentY)
	rectangle(x + indentX/2, y + indentY/2 - height/6, x + width/2 - indentX, y + height/2 - indentY)

def draw_clew(x, y, size):
	brushColor(lgr_clr)
	penColor(grey_clr)
	draw_oval(x, y, size, size)

	# Thread
	penColor(lgr_clr)
	draw_thread(x - size/2, y + size/2, size*3, -math.pi*23/24)

	# Lines on clew
	penColor(grey_clr)
	draw_curve(x, y - size*2/3, size, -math.pi*0.4, 0)
	draw_curve(x, y - size*0.55, size, -math.pi*0.4, -math.pi/12)
	draw_curve(x, y - size*0.45, size, -math.pi*0.4, -math.pi/6)
	draw_curve(x, y, size, math.pi*0.3, -math.pi*0.75)
	draw_curve(x - size/10, y - size/10, size, math.pi*0.3, -math.pi*0.85)
	draw_curve(x + size/10, y + size/10, size, math.pi*0.25, -math.pi*0.65)
