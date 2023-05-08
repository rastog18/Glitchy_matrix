import turtle
from turtle import Turtle, Screen

obj = Turtle()
screen = Screen()
def forward():
    obj.forward(20)
def backward():
    obj.backward(20)
def counter_clockwise():
    a = obj.heading()
    a += 20
    obj.setheading(a)
def clockwise():
    a = obj.heading()
    a -= 10
    obj.setheading(a)
def clear():
    screen.reset()

screen.listen()
screen.onkey(key = "A",fun = counter_clockwise)
screen.onkey(key = "D",fun = clockwise)
screen.onkey(key = "C",fun = clear)
screen.onkey(key = "W",fun = forward)
screen.onkey(key = "S",fun = backward)
screen.exitonclick()
