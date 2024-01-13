from hirst_painting import color_list
import random
import turtle as t


def row_dot():
    for cnt in range(10):
        ray.pendown()
        r_color = random.choice(color_list)
        ray.dot(dot_size, r_color)
        ray.penup()
        if cnt != 9:
            ray.forward(50)


def dot_printing(x, y):
    for col in range(10):
        row_dot()
        y += 50
        ray.penup()
        if col != 9:
            ray.setpos(x, y)


t.colormode(255)
ray = t.Turtle()
dot_size = 20
start_x = -300
start_y = -300
ray.penup()
ray.setpos(start_x, start_y)
dot_printing(start_x, start_y)
screen = t.Screen()
screen.exitonclick()

