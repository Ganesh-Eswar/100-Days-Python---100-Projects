import turtle as t


class Paddle(t.Turtle):
    def __init__(self,start_x,start_y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.color('white')
        self.penup()
        self.goto(x=start_x, y=start_y)

    def go_up(self):
        if self.ycor() <= 240:
            self.forward(20)

    def go_down(self):
        if self.ycor() > -240:
            self.backward(20)


