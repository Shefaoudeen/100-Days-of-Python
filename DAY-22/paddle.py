from turtle import Turtle
DISPLACEMENT = 40


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def on_up(self):
        already_y = self.ycor()
        self.goto(self.xcor(), already_y+DISPLACEMENT)

    def on_down(self):
        already_y = self.ycor()
        self.goto(self.xcor(), already_y-DISPLACEMENT)
