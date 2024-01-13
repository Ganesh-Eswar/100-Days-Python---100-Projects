import turtle as t

ray = t.Turtle()


def move_forward():
    ray.forward(10)


def move_backward():
    ray.backward(10)


def counter_closkwise():
    global angle
    angle += 10
    ray.setheading(angle)


def closkwise():
    global angle
    angle -= 10
    ray.setheading(angle)


def clear_draw():
    t.resetscreen()


angle = 0
screen = t.Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_closkwise)
screen.onkey(key='d', fun=closkwise)
screen.onkey(key='c', fun=clear_draw)
screen.exitonclick()
