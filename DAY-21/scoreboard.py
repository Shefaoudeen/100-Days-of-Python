from turtle import Turtle

highscore = None

with open('data.txt') as file:
    highscore = int(file.read())


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.high_score = highscore
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.points} High Score = {self.high_score}", align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open('data.txt',mode='w') as data:
                data.write(str(self.high_score))
        self.points = 0
        self.update_scoreboard()
