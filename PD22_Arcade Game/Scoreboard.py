from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

    def score1(self, variable):
        self.clear()
        self.goto(-30, 200)
        self.write(arg=f"{variable}", align="center", font=('Comic Sans', 50, 'normal'))

    def score2(self, variable):
        self.goto(30, 200)
        self.write(arg=f"{variable}", align="center", font=('Comic Sans', 50, 'normal'))

    def game_over(self, variable1):
        self.goto(0, 0)
        self.screen.bgcolor("black")
        self.write(arg="Game Over.", move=False, align='Center', font=('Verdana', 20, 'normal'))
        self.goto(0,-30)
        if variable1 == 11:
            self.write(arg=f"Player 1 Won", move=False, align='Center', font=('Verdana', 10, 'normal'))
        else:
            self.write(arg=f"Player 2 Won", move=False, align='Center', font=('Verdana', 10, 'normal'))
