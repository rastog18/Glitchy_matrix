from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.penup()

    def food_posit(self):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.setposition(x, y)



