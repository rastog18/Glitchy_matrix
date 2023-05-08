from turtle import Turtle,Screen,colormode
import random
def color():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    t = (a, b, c)
    return (t)

obj = Turtle()
screen = Screen()
colormode(255)
obj.speed("fastest")
a = 0
while a != 360:
    t= color()
    obj.color(t)
    obj.circle(100)
    obj.setheading(a)
    a += 2

screen.exitonclick()
