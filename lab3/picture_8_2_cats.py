from graph import *
import math

from utils import *

width, height = windowSize()

# Background
brushColor(mg_clr)
rectangle(0, 0, width, height * 0.45)
brushColor(mryel_clr)
rectangle(0, height * 0.45, width, height)


#CLEW
draw_clew(420, 540, width / 10)
draw_clew(420, 400, width / 10 / 4)
draw_clew(180, 380, width / 10 / 2)
draw_clew(220, 550, width / 10 / 4)

# CATS
draw_cat(350, 320, 170 / 2, 170 / 2, op_clr)
draw_cat(70, 390, -170 / 4, 170 / 4, op_clr)
draw_cat(120, 500, -170 / 2, 170 / 2, cgr_clr)
draw_cat(290, 420, 170 / 3, 170 / 3, cgr_clr)
draw_cat(120, 300, -1*170 / 3, 170 / 3, cgr_clr)



#WINDOWS
draw_window( 250 + width * 0.28, height * 0.23, width * 0.4, height * 0.4)
draw_window( 20 + width * 0.28, height * 0.23, width * 0.4, height * 0.4)
draw_window( -210 + width * 0.28, height * 0.23, width * 0.4, height * 0.4)


run()
