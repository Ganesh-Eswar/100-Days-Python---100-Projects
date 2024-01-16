import random
import turtle as t
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(start_x=350, start_y=0)
l_paddle = Paddle(start_x=-350, start_y=0)
ball = Ball(x=0, y=0)
score_label = Score(x=-100, y=200, text='SCORE')
l_score = Score(x=-200, y=200, text=0)
r_score = Score(x=200, y=200, text=0)

screen.listen()
screen.onkey(key='Up', fun=r_paddle.go_up)
screen.onkey(key='Down', fun=r_paddle.go_down)
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)
is_game_on = True
ball_angle = 0
ver_flag = False

start_time = time.time()
speed = 1
while is_game_on:
    screen.update()
    ball.move(ball_angle)
    time.sleep(0.01)
    if abs(ball.ycor()) < 270:
        ver_flag = True
    if l_paddle.distance(ball) < 40 or r_paddle.distance(ball) < 40:
        if l_paddle.distance(ball) < 40:
            l_score.update_score()
        else:
            r_score.update_score()
        ball_angle = 180 - ball_angle
        error = random.randint(-10, 10)
        ball_angle += error
    if ver_flag:
        if abs(ball.xcor()) < 350 and 290 < abs(ball.ycor()):
            ball_angle = 360 - ball_angle
            ver_flag = False
    if abs(ball.xcor()) > 390:
        game_over = Score(x=-200, y=0, text='GAME OVER')
        is_game_on = False
    end_time = time.time()
    hours, rem = divmod(end_time - start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    if int(minutes) % 2 == 0 and minutes > 0:
        print(int(minutes))
        speed += 1
        ball.speed(speed)
        print(speed)
screen.exitonclick()
