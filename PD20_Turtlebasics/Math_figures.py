from turtle import Turtle, Screen
import random

obj = Turtle()
screen = Screen()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw(angle, sides):
    for i in range(20):
        turn = 180 - (angle / sides)
        init = obj.pos()
        this = color()
        obj.color(this)
        obj.forward(40)
        while obj.distance(init) > 1:
            obj.right(turn)
            obj.forward(40)
        if obj.distance(init) < 1:
            obj.right(turn)
        angle += 180
        sides += 1


def color():
    global colours
    return (random.choice(colours))


angle = 180
sides = 3
draw(angle, sides)
screen.exitonclick()
