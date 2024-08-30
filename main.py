from turtle import Screen
from paddle import Paddel
from ball import Ball
from scoreboard import Score
import time
screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_padel = Paddel((350, 0))
l_padel = Paddel((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_padel.go_up, "Up")
screen.onkeypress(r_padel.go_down, "Down")
screen.onkeypress(l_padel.go_up, "w")
screen.onkeypress(l_padel.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()

    # bounce with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collisoin with padels
    if ball.xcor() > 325 and ball.distance(r_padel) < 50 or ball.xcor() < -325 and ball.distance(l_padel) < 50:
        ball.bounce_x()

    # ball misses
    if ball.xcor() > 380:
        ball.out()
        score.l_point()

    if ball.xcor() < -390:
        ball.out()
        score.r_point()


screen.exitonclick()
