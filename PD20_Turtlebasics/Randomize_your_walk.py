from turtle import Turtle,Screen
import random

obj = Turtle()
obj.width(5)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
direction = [90,180,270,360]
def randomized_walk(colours,direction):
    while True:
        obj.color(random.choice(colours))
        obj.right(random.choice(direction))
        obj.forward(15)

randomized_walk(colours,direction)
