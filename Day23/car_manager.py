import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allCars = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def generateCar(self):
        if random.randint(0, 10) > 8:
            startPosition = (270, random.randint(-280, 280))
            turtle = Turtle()
            turtle.pu()
            turtle.seth(180)
            turtle.shape("square")
            turtle.shapesize(stretch_len=2)
            turtle.color(random.choice(COLORS))
            turtle.setpos(startPosition)
            self.allCars.append(turtle)

    def moveCars(self):
        for car in self.allCars:
            car.forward(self.carSpeed)

    def increaseSpeed(self):
        self.carSpeed += MOVE_INCREMENT
