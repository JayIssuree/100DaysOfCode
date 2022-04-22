from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

lpaddle = Paddle(-350)
rpaddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
rpaddleStart = True

while game_is_on:
    screen.onkey(lpaddle.move_up, "w")
    screen.onkey(lpaddle.move_down, "s")
    screen.onkey(rpaddle.move_up, "Up")
    screen.onkey(rpaddle.move_down, "Down")
    ball.move()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.increment_lscore()
    
    if ball.xcor() < -350:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.increment_rscore()

    screen.update()

screen.exitonclick()