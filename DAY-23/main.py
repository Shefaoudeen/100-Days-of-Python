import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

level = Scoreboard()
player = Player()
cars = CarManager()

screen.listen()

screen.onkey(fun= player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    if player.ycor() > 280:
        player.next_level()
        level.next_level()
        cars.next_level()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            level.game_over()
            player.starting_pos()
            cars.disapper()
            game_is_on = False

    if level.level > 10:
        level.winner()
        cars.disapper()
        game_is_on = False

    cars.create_cars()
    cars.move_forward()
    screen.update()

screen.exitonclick()
