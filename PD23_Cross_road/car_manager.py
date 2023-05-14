from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black", random.choice(COLORS))
        self.hideturtle()
        self.goto(275, random.randint(-250, 230))
        self.car_shape()

    def car_shape(self):
        self.speed("fastest")
        self.begin_fill()
        self.forward(10)
        self.right(90)
        self.circle(8, 180)
        self.right(85)
        self.forward(5)
        self.left(65)
        self.forward(10)
        self.setheading(180)
        self.forward(10)
        self.setheading(120)
        self.forward(10)
        self.setheading(180)
        self.forward(25)
        self.setheading(240)
        self.forward(10)
        self.setheading(180)
        self.forward(10)
        self.setheading(290)
        self.forward(10)
        self.setheading(355)
        self.forward(5)
        self.setheading(270)
        self.circle(8, 180)
        self.setheading(0)
        self.forward(12.5)
        self.end_fill()

    def car_move(self, STARTING_MOVE_DISTANCE):
        self.clear()
        self.backward(STARTING_MOVE_DISTANCE)
        self.car_shape()
