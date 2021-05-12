import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# create the screen

wn = Screen()
wn.tracer(0)
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.title("Pong game")
wn.listen()

scoreboard = Scoreboard()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
wn.onkeypress(r_paddle.up, "Up")
wn.onkeypress(r_paddle.down, "Down")
wn.onkeypress(l_paddle.up, "w")
wn.onkeypress(l_paddle.down, "s")
game_is_on = True
while game_is_on:
    wn.update()
    ball.move()
    time.sleep(ball.pace)

    # detect collision with the  top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect when l_paddle misses

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

wn.exitonclick()
