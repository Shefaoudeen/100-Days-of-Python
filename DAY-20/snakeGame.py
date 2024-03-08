from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake_body = Snake()

screen.listen()
screen.onkey(snake_body.up, "Up")
screen.onkey(snake_body.down, "Down")
screen.onkey(snake_body.right, "Right")
screen.onkey(snake_body.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake_body.snake_move()

screen.exitonclick()
