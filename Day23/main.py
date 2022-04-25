import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, "Up")
    car_manager.generateCar()
    car_manager.moveCars()
    if player.levelComplete():
        car_manager.increaseSpeed()
        scoreboard.level_up()
    for car in car_manager.allCars:
        if player.check_collision(car):
            game_is_on = False


scoreboard.game_over()
screen.exitonclick()