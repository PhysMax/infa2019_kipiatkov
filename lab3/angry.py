# All rights is not reserved. Read ./COPYRIGHT

# Draw "angry smile"

from graph import *
import math

width, height = windowSize()
center = width / 2, height / 2

def draw_rect(startX:'float', startY:'float',
		width:'float', height:'float',
		angle:'float'=0)->'int':
	""" Draw rectangle width * height starting from (startX, startY) with rotated 	to angle (in radians). Return link to rectangle. """
	s = math.sin(angle)
	c = math.cos(angle)
	return polygon([(startX, startY),
	(startX + width * c, startY - width * s),
	(startX + width * c + height * s, startY - width * s + height * c),
	(startX + height * s, startY + height * c)])


if __name__ == '__main__':
	penColor('black')
	# Draw face
	brushColor('yellow')
	R = width/4
	circle(center[0], center[1], R)

	# Draw left eyes
	left_eye = center[0] - R*0.4, center[1] - R/4
	brushColor('red')
	circle(left_eye[0], left_eye[1], R/5)
	brushColor('black')
	circle(left_eye[0], left_eye[1], R/15)
	draw_rect(left_eye[0] + R*0.4, left_eye[1], R, R/7, 5*math.pi/6)

	# Draw right eye
	right_eye = center[0] + R*0.4, center[1] - R/4
	brushColor('red')
	circle(right_eye[0], right_eye[1], R/7)
	brushColor('black')
	circle(right_eye[0], right_eye[1], R/15)
	draw_rect(right_eye[0] - R*2/7, right_eye[1], R*2/3, -R/10, math.pi/7)

	# Draw mouth
	draw_rect(center[0] - R/2, center[1] + R/3, R, R/5)

	run()
