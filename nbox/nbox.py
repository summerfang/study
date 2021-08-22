import turtle

def box_combination(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n has to be positive integer")

    qualified_combination = list()

    for i in range(1, n + 1):
        y = 1

        while i * y < n:
            y = y + 1
        
        item = list()
        item.append(i)
        item.append(y)

        qualified_combination.append(item)

    return qualified_combination

def get_row_column_make_area_biggest(GW, GH, n, list_row_col, ratio):
    list_areas = list()

    for item in list_row_col:
        row = item[0]
        col = item[1]

        w = GW/col
        h_by_ratio = w / ratio

        h = GH/row

        if h_by_ratio >= h:
            height = h
        else:
            height = h_by_ratio

        width = height * ratio

        area = width * height * n
        list_areas.append(area)

    max_area = max(list_areas)
    max_index = list_areas.index(max_area)

    return list_row_col[max_index]

# for i in range(1, 25):
#     print(str(i) + ":")
#     print(box_combination(i))

GW = 64
GH = 48
n = 10
ratio = 16/9 

item = get_row_column_make_area_biggest(GW, GH, n, box_combination(n), ratio)

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