from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")


line = Turtle(visible=False)
line.color("white")
line.pensize(7)
line.penup()
line.goto(0, -290)

for _ in range(30):
    line.pendown()
    line.sety(line.ycor() + 15)
    line.penup()
    line.sety(line.ycor() + 15)



right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

def collision():
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 and ball.xcor() > 0:
        ball.bounce(-1)
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -330 and ball.xcor() < 0:
        ball.bounce(1)
    elif ball.xcor() > 420 or ball.xcor() < -420:
        if ball.xcor() < 0:
            scoreboard.update_scoreboard(1)
        else:
            scoreboard.update_scoreboard(0)
        ball.goto(0, 0)
        ball.setheading(random.randrange(-360, 360, 20))
        ball.speed += 1
        left_paddle.speed += 1
        right_paddle.speed += 1


def tick():
    if scoreboard.scores[0] >= 10 or scoreboard.scores[1] >= 10:
        screen.bye()
    ball.motion()
    collision()

    for action in keys_pressed:
        actions[action]()

    screen.update()
    screen.ontimer(tick, frame_delay_ms)


frame_delay_ms = 1000 // 30  # default for turtle is 10 in _CFG["delay"]
actions = dict(
    r_up=lambda: right_paddle.up(),
    r_down=lambda: right_paddle.down(),
    l_up=lambda: left_paddle.up(),
    l_down=lambda: left_paddle.down(),
)

keys_pressed = set()
screen.onkeypress(lambda: keys_pressed.add("r_up"), "Up")
screen.onkeypress(lambda: keys_pressed.add("r_down"), "Down")
screen.onkeypress(lambda: keys_pressed.add("l_up"), "w")
screen.onkeypress(lambda: keys_pressed.add("l_down"), "s")

screen.onkeyrelease(lambda: keys_pressed.remove("r_up"), "Up")
screen.onkeyrelease(lambda: keys_pressed.remove("r_down"), "Down")
screen.onkeyrelease(lambda: keys_pressed.remove("l_up"), "w")
screen.onkeyrelease(lambda: keys_pressed.remove("l_down"), "s")

screen.listen()
tick()

screen.exitonclick()