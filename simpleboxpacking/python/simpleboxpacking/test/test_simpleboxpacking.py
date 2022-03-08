import sys
sys.path.insert(1, './src/')

from simpleboxpacking import SimpleBoxPacking 

import pytest

@pytest.fixture
def simpleboxpacking():
    box_packing = SimpleBoxPacking(192, 108, 1, 16/9)
    return box_packing

# def test_get_integer_pairs_which_product_is_no_more_than_n(simpleboxpacking):
#     for n in range(1,26):
#         pairs = simpleboxpacking.get_integer_pairs_which_product_is_no_more_than_n(n)
#         print(pairs)

#     assert True

# def test_w_1080p(simpleboxpacking):
#     assert simpleboxpacking.row == 1
#     assert simpleboxpacking.col == 1
#     assert simpleboxpacking.w == 960
#     assert simpleboxpacking.h == 540

#     simpleboxpacking.set_n(2)
#     assert simpleboxpacking.row == 1
#     assert simpleboxpacking.col == 2

#     simpleboxpacking.set_n(3)
#     assert simpleboxpacking.row == 2
#     assert simpleboxpacking.col == 2

#     simpleboxpacking.set_n(5)
#     assert simpleboxpacking.row == 2
#     assert simpleboxpacking.col == 3

import turtle

def test_5by5_and_108by192_with_16by9(simpleboxpacking):
    t = turtle.Turtle()
    t.speed(0)

    simpleboxpacking.set_WH(108, 192)
    simpleboxpacking.set_np(25, 16/9)

    for i in range(1,26):
        draw_n(simpleboxpacking, i, t)
        t.clear()

def test_5by5_and_192by108_with_16by9(simpleboxpacking):
    t = turtle.Turtle()
    t.speed(0)

    simpleboxpacking.set_WH(192, 108)
    simpleboxpacking.set_np(26, 16/9)

    for i in range(1,26):
        draw_n(simpleboxpacking, i, t)
        t.clear()

def test_5by5_and_64by48_with_4by3(simpleboxpacking):
    t = turtle.Turtle()
    t.speed(0)

    simpleboxpacking.set_WH(64, 48)
    simpleboxpacking.set_np(26, 4/3)

    for i in range(1,26):
        draw_n(simpleboxpacking, i, t)
        t.clear()

def test_5by5_and_48by64_with_16by9(simpleboxpacking):
    t = turtle.Turtle()
    t.speed(0)

    simpleboxpacking.set_WH(48, 64)
    simpleboxpacking.set_np(26, 4/3)

    for i in range(1,26):
        draw_n(simpleboxpacking, i, t)
        t.clear()

def draw_n(simpleboxpacking, n, t):
    simpleboxpacking.set_n(n)
    
    w = simpleboxpacking.w
    h = simpleboxpacking.h
    row = simpleboxpacking.row
    col = simpleboxpacking.col

    t.pencolor("blue")
    draw_rectangle(t, 0, 0, simpleboxpacking.W, simpleboxpacking.H)        

    count = 0
    start_x = 0
    start_y = 0
    for r in range(row):
        t.up()
        t.goto(0,0)

        t.pencolor("red")
        for c in range(col):
            count += 1
            if count > n:
                break
        
            start_x = c*w
            start_y = r*h
            
            draw_rectangle(t, start_x, start_y, w, h)
 
def draw_rectangle(t, start_x, start_y, width, height):
    t.up()
    t.goto(start_x, start_y)
    t.down()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.up()