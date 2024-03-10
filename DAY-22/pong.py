from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()
r_block = Paddle((350, 0))
l_block = Paddle((-350, 0))
screen.update()
ball = Ball()
screen.listen()

screen.onkey(r_block.on_up, "Up")
screen.onkey(r_block.on_down, "Down")
screen.onkey(l_block.on_up, "w")
screen.onkey(l_block.on_down, "s")

game_on = True

while game_on:
    time.sleep(0.05)

    if ball.xcor() > 380:
        score.l_point()
        ball.check_edge()

    if ball.xcor() < -380:
        score.r_point()
        ball.check_edge()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_diry()

    ball.move()

    if ball.distance(r_block) < 40 and ball.xcor() > 320 and ball.movement_x > 0:
        ball.change_dirx()
        ball.movement_x *= 1.05

    if ball.distance(l_block) < 40 and ball.xcor() < -320 and ball.movement_x < 0:
        ball.change_dirx()
        ball.movement_x *= 1.05

    screen.update()

screen.exitonclick()
