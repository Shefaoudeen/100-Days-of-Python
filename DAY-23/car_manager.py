from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.num = 11

    def create_cars(self):
        random_int = random.randint(1, self.num)
        if random_int == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def disapper(self):
        self.all_cars = []

    def next_level(self):
        self.num -= 1
