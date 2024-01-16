from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y, text):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(x=x, y=y)
        self.update_text(text)

    def update_text(self, text):
        self.write(f"{text}", font=('classic', 50, 'normal'))


    def update_score(self):
        self.score += 1
        self.clear()
        self.update_text(text=self.score)
