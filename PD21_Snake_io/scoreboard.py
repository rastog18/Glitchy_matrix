from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 225)

    def score(self,variable):
        self.clear()
        self.write(arg=f"Score:{variable}", align="center", font=('Verdana', 20, 'normal'))

    def game_over(self,variable):
        self.score(variable)
        self.goto(0,0)
        self.screen.bgcolor("black")
        self.write(arg="Game Over.", move=False, align='Center', font=('Verdana', 20, 'normal'))
