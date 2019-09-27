from graph import *
import math

penColor('black')


def rotate_oval(a, b, xcenter, ycenter):  # a - size Ox semiaxis, b - size Oy semiaxis
    points = []

    for fi in range(0, 628):  # fi/100 - angle of rotation
        x = a * math.cos(fi / 100)
        y = b * math.sin(fi / 100)
        points.append((x + xcenter, y + ycenter))
    polygon(points)


rotate_oval(150, 100,150, 150)

run()
