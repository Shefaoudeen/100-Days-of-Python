from turtle import Turtle
STARTING_POSITION = [(0,0),(0,-20),(0,-40)]

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_create()
        self.head = self.segments[0]

    def snake_create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        seg = Turtle()
        seg.shape("square")
        seg.penup()
        seg.color("white")
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        direction = self.head.heading()
        if direction == 0:
            self.head.left(90)
        elif direction == 180:
            self.head.right(90)

    def down(self):
        direction = self.head.heading()
        if direction == 180:
            self.head.left(90)
        elif direction == 0:
            self.head.right(90)

    def right(self):
        direction = self.head.heading()
        if direction == 270:
            self.head.left(90)
        elif direction == 90:
            self.head.right(90)

    def left(self):
        direction = self.head.heading()
        if direction == 90:
            self.head.left(90)
        elif direction == 270:
            self.head.right(90)


