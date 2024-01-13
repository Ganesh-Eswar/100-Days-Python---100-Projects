from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.write(f"Score is {self.score}", align='center',font=('Arial',15,'normal'))
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over", align='center', font=('Arial', 15, 'normal'))

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f"Score is {self.score}", align='center',font=('Arial',15,'normal'))



