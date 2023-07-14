from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__("square")
        self.speed = 25
        self.create_paddle(x)

    def create_paddle(self, x):
        self.color("white")
        self.penup()
        self.goto(x, 0)
        self.turtlesize(5, 1)

    def up(self):
        if not self.ycor() >= 250:
            self.sety(self.ycor() + self.speed)

    def down(self):
        if not self.ycor() <= -250:
            self.sety(self.ycor() + -self.speed)
