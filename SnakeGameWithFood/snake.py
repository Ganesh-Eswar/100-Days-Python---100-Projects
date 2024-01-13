import turtle as t 

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.x, self.y = 0, 0
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for _ in range(3):
            new_tur = t.Turtle()
            new_tur.penup()
            new_tur.shape('square')
            new_tur.color('white')
            new_tur.setpos(x=self.x, y=self.y)
            self.x -= 20
            self.turtles.append(new_tur)
            
    def move_snake(self):

        for index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[index - 1].xcor()
            new_y = self.turtles[index - 1].ycor()
            self.turtles[index].goto(x=new_x, y=new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        current_head = int(self.head.heading())
        if current_head != DOWN:
            self.head.setheading(UP)

    def down(self):
        current_head = int(self.head.heading())
        if current_head != UP:
            self.head.setheading(DOWN)

    def right(self):
        current_head = int(self.head.heading())
        if current_head != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        current_head = int(self.head.heading())
        if current_head != RIGHT:
            self.head.setheading(LEFT)

    def add_body(self):
        new_tur = t.Turtle()
        new_tur.penup()
        new_tur.shape('square')
        new_tur.color('white')
        pos_x, pos_y = (self.turtles[-1]).xcor(), (self.turtles[-1]).ycor()
        new_tur.setpos(x=pos_x-20, y=self.y)
        self.turtles.append(new_tur)
