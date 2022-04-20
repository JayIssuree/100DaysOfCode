from turtle import Turtle, Screen
import random

is_race_on = True

screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            print("The " + winning_colour + " turtle won!")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()