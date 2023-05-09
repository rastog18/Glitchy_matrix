from turtle import Turtle
import random, time

x = 10
class Snake:
    def __init__(self):
        self.snake_body = []
        self.heading = 0
        self.snake_head = None

    def color(self):
        """The Function is for the random colors of the balls."""
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        t = (a, b, c)
        return (t)

    def posit(self):
        """The Function is to ensure that whenever the snake grows, the _growth_ is added to its tail only."""
        if not self.snake_body:
            position = [0, 0]
            return position
        else:
            position = (self.snake_body[-1]).pos()
            return position

    def create_body(self):
        """The Function creates new objects with desired characteristics."""
        body = Turtle()
        body.speed("fastest")
        body.color(self.color())
        body.shape("circle")
        position = list(self.posit())
        # I am not sure why the line below works for every case, I tought that while turning right, I should have: position[1] -= 10.
        position[0] -= x
        body.penup()
        self.snake_body.append(body)
        body.setposition(tuple(position))
        body.setheading(self.heading)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].forward(x)
            if self.snake_body[i].heading() != (self.snake_body[i - 1]).heading:
                head = (self.snake_body[i - 1]).heading()
                self.snake_body[i].setheading(head)
        self.snake_body[0].forward(x)


    def turn_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
        else:
            pass

    def turn_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
        else:
            pass

    def turn_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)
        else:
            pass

    def turn_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
        else:
            pass

    def begin(self):

        for i in range(3):
            self.create_body()
        self.snake_head = self.snake_body[0]

#I will add an easier and difficult ersion to this easy speed =10, hard speed =20
