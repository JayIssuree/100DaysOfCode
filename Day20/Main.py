from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

game_is_on = True

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    for body in snake.snake[1:]:
        if snake.head.distance(body) < 10:
            score.reset()
            snake.reset()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_tail()
        score.update()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

screen.exitonclick()