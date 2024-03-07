import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'indigo']
all_turtle = []

i = 0

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-150 + i)
    all_turtle.append(new_turtle)
    i += 50

game_on = True

while game_on:

    for turtles in all_turtle:

        if turtles.xcor() >= 230:
            if turtles.pencolor() == bet:
                print(f"You've won the game. The winner is {turtles.pencolor()}")
            else:
                print(f"You've lost the game. The winner is {turtles.pencolor()}")
            game_on = False

        movement = random.randint(1,10)
        turtles.forward(movement)

screen.exitonclick()
