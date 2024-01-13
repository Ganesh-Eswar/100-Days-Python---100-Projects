import turtle as t
import random


screen = t.Screen()
user_input = screen.textinput(title='Take your bet!', prompt='which turtle will win the race? Type your color: ')
screen.setup(width=500, height=400)
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

x_pix = -230
y_pix = [pix for pix in range(150, -200, -50)]

turtles = dict()

for turtle_index in range(len(color)):
    tur = t.Turtle(shape='turtle')
    tur.color(color[turtle_index])
    tur.penup()
    tur.goto(x=x_pix, y=y_pix[turtle_index])
    turtles[turtle_index] = tur

winner = None
is_end = False

while not is_end:
    random_walk = [random.randint(0, 5) for _ in range(6)]
    for i in range(len(random_walk)):
        turtles[i].forward(random_walk[i])
        if turtles[i].xcor() > 225:
            winner = i
            is_end = True
            break

if winner == color.index(user_input):
    print(f'You won the winner is {color[winner]} turtle!')
else:
    print(f'You loss the winner is {color[winner]} turtle!')

screen.exitonclick()
