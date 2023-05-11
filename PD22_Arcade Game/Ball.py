from turtle import Turtle,Screen
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()


    def move(self, paddle1, paddle2, p1, p2):
        x = 10
        y = 10
        c = 0.06
        self.hideturtle()
        self.goto(0, random.randint(-100, 100))
        self.showturtle()
        game_is_on = True
        while game_is_on:
            new_x = self.xcor() + x
            new_y = self.ycor() + y
            self.goto(new_x, new_y)
            Screen().update()
            time.sleep(c)
            if 230 < self.ycor() or self.ycor() < -230:
                y *= -1
            if self.distance(paddle1) < 40 and self.xcor() < -355:
                x *= -1
                c -= 0.01
            elif self.distance(paddle2) < 40 and self.xcor() > 355:
                x *= -1
                c -= 0.002
            if self.xcor() > 365:
                p1 += 1
                game_is_on = False

            elif self.xcor() < -365:
                p2 += 1
                game_is_on = False

        return p1, p2

