"""
import colorgram

colors = colorgram.extract('color-platte.jpg', 25)
color_list = []

for color in colors:
    rgb = color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    tuples = (red, green, blue)
    color_list.append(tuples)

print(color_list)
"""

import random
import turtle as t

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

timmy = t.Turtle()
screen = t.Screen()

screen.colormode(255)
timmy.speed('fastest')
timmy.hideturtle()


y = 0

for i in range(10):
    timmy.penup()
    timmy.setposition(-200, -200+y)
    timmy.pendown()
    for j in range(10):
        random_color = random.choice(color_list)
        timmy.pencolor(random_color)

        timmy.fillcolor(random_color)
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    y += 50


screen.exitonclick()
