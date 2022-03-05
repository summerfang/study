import turtle
from nbox import *

# for i in range(1, 25):
#     print(str(i) + ":")
#     print(box_combination(i))

GW = 64
GH = 48
n = 10
ratio = 16/9 

item = get_row_column_make_area_biggest(GW, GH, n, ratio)

tl = turtle.Turtle()
tl.speed(0)
tl.forward(GW)
tl.left(90)
tl.forward(GH)
tl.left(90)
tl.forward(GW)
tl.left(90)
tl.forward(GH)
tl.left(90)

height = GH/item[0]
width = GW/item[1]

w = height * ratio
h = width/ratio

if height <= h:
    width = height * ratio
else:
    height = width/ratio

turtle.pencolor("red")

count = 0
for r in range(0, item[0]):
    tl.up()
    tl.goto(0,0)
    for c in range(0, item[1]):
        count = count + 1
        if count > n:
            break

        tl.goto(c*width, r*height)
        tl.down()
        tl.forward(width)
        tl.left(90)
        tl.forward(height)
        tl.left(90)
        tl.forward(width)
        tl.left(90)
        tl.forward(height)
        tl.left(90)
        tl.up()

turtle.done()