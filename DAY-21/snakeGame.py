from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake_body = Snake()
food = Food()
scores = Scoreboard()

screen.listen()
screen.onkey(snake_body.up, "Up")
screen.onkey(snake_body.down, "Down")
screen.onkey(snake_body.right, "Right")
screen.onkey(snake_body.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake_body.snake_move()

    if snake_body.head.distance(food) < 15:
        food.refresh()
        snake_body.extend()
        scores.increase_score()

    if snake_body.head.xcor() > 280 or snake_body.head.xcor() < -280:
        scores.reset()
        snake_body.reset()

    if snake_body.head.ycor() > 280 or snake_body.head.ycor() < -280:
        scores.reset()
        snake_body.reset()

    for segment in snake_body.segments[1:]:

        if snake_body.head.distance(segment) < 10:
            scores.reset()
            snake_body.reset()

screen.exitonclick()
