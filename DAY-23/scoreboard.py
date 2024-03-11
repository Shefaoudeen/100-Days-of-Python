from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.update_level()

    def update_level(self):
        self.write(f"Level {self.level}", font=FONT, align="left")

    def next_level(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def winner(self):
        self.clear()
        self.home()
        self.write("WE HAVE A WINNER", align="center", font=FONT)
