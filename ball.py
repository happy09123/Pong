from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.setheading(50)
        self.speed = 10

    def motion(self):
        if self.ycor() > 280:
            self.setheading(360 - self.heading())
        if self.ycor() < -280:
            self.setheading(-360 - self.heading())

        self.forward(self.speed)

    def bounce(self, n):
        self.setheading(180 - self.heading() * n)
