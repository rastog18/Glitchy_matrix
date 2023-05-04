import colorgram
from turtle import Turtle,colormode,Screen
import random


colors = colorgram.extract("img.jpeg",10)
color_list = []
for i in colors:
    t = (i.rgb.r,i.rgb.g,i.rgb.b)
    color_list.append(t)
print(color_list)

colormode(255)
obj = Turtle()
screen = Screen()
obj.speed("fastest")
obj.penup()
obj.setposition(-250,-200)
c = 0
for i in range(10):
    for i in range(10):
        t = random.choice(color_list)
        obj.dot(20,t)
        obj.forward(50)
    c +=1
    if (c % 2) == 0:
        obj.right(90)
        obj.forward(50)
        obj.right(90)
        obj.forward(50)
    else:
        obj.left(90)
        obj.forward(50)
        obj.left(90)
        obj.forward(50)

screen.exitonclick()
