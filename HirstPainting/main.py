import turtle
from turtle import Turtle, Screen
from math import ceil
import random


def square(side):
    for _ in range(4):
        maaza.forward(side)
        maaza.right(90)


def dashed_line(line_px):
    total_dots = ceil(line_px / 10)
    for i in range(total_dots):
        if i % 2 == 0:
            maaza.pendown()
            maaza.forward(10)
        else:
            maaza.penup()
            maaza.forward(10)


def polygon_draw(polygon_size,move_pixel):
    for side in range(3, polygon_size + 1):
        angle = 360 / side
        r, g, b = [random.randint(0, 255) / 255 for _ in range(3)]
        for draw in range(side):
            maaza.pencolor(r, g, b)
            maaza.forward(move_pixel)
            maaza.right(angle)


def random_path(move_size):
    while True:
        movement = random.randint(1,4)
        if movement == 1:
            maaza.forward(move_size)
        elif movement == 2:
            maaza.backward(move_size)
        elif movement == 3:
            maaza.right(90)
            maaza.forward(move_size)
        else:
            maaza.left(90)
            maaza.forward(move_size)
        r, g, b = [random.randint(0, 255) for _ in range(3)]
        maaza.pencolor(r, g, b)


def draw_spirograph(radius):
    for angle in range(0, 361):
        r, g, b = [random.randint(0,255) for _ in range(3)]
        maaza.pencolor(r,g,b)
        maaza.right(angle)
        maaza.circle(radius)


turtle.colormode(255)
maaza = Turtle()
maaza.shape('turtle')
maaza.color('red', 'black')
maaza.speed('fastest')

# maaza.pensize(5)
# square(100)
# dashed_line(234)
# polygon_draw(20,50)
# random_path(30)
draw_spirograph(50)


screen = Screen()
screen.exitonclick()
