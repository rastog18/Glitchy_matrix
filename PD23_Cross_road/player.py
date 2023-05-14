from turtle import Turtle,Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.color("turquoise")
        self.left(90)

    def move_turtle(self):
        self.forward(10)
        Screen().update()


