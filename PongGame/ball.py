from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('white')
        self.goto(x=x, y=y)

    def move(self, angle):
        self.setheading(angle)
        self.forward(3)

    def inc_speed(self, level):
        self.speed(level)