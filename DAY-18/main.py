from turtle import Turtle,Screen
import random


timmy = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy.speed("fastest")

rotate = 100
i = 0
angle = 360/rotate

while i <= rotate:
    random_color = random.choice(colors)
    timmy.color(random_color)
    timmy.circle(75)
    timmy.right(angle)
    i += 1

screen = Screen()
screen.exitonclick()
