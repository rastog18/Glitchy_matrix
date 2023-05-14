from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")

    def score(self,c):
        self.clear()
        self.goto(-250, 250)
        self.write(arg=f"Level:{c} ", font=FONT)

    def collision(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over. ", align="center", font=FONT)
