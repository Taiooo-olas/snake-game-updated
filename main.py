from turtle import Turtle, Screen
from link import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.bgcolor("black")
screen.screensize(canvwidth=600, canvheight=600)
screen.title("Snake")
screen.tracer(0)


snake = Snake()
score = ScoreBoard()
munch = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_running = True
while True:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()

    # Detect Food

    if snake.head.distance(munch) < 15:
        munch.refresh()
        snake.extend()
        score.increase_score()

    # special ball

    if score.score == score.double - 1:
        munch.special_ball()
        score.print_extra()

    # Reward extra points

    if score.score == score.double:
        score.extra_points()
        munch.color("blue")

    # Distance to wall

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_running = False
        score.game_over()
        munch.color("black")
        break

    # distance to self

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            score.game_over()
            munch.color("black")
            break


screen.exitonclick()





