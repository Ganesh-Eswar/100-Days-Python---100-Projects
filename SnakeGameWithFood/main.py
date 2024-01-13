import turtle as t
import time
from snake import Snake
from food import Food
from ScoreBoard import Score

screen = t.Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.title("Snake with food!")
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left',  fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        # include one body part to snake
        snake.add_body()

    # detect collision with wall
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    if head_x > 300 or head_x < -300 or head_y > 300 or head_y < -300:
        is_game_on = False
        score.game_over()

    # detect collision with own body
    turtle_body_co_ords = []
    for index in range(1, len(snake.turtles)):
        x = snake.turtles[index].xcor()
        y = snake.turtles[index].ycor()
        turtle_body_co_ords.append((x, y))
    if (head_x, head_y) in turtle_body_co_ords:
        is_game_on = False
        score.game_over()

screen.exitonclick()
