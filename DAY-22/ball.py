from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movement_x = 10
        self.movement_y = 10

    def move(self):
        self.goto(self.xcor()+self.movement_x, self.ycor()+self.movement_y)

    def change_diry(self):
        self.movement_y *= -1

    def change_dirx(self):
        self.movement_x *= -1

    def check_edge(self):
        self.home()
        if self.movement_x > 0:
            self.movement_x = 10
        else:
            self.movement_x = -10
        self.change_dirx()

