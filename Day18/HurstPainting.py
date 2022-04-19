from turtle import Screen, Turtle
import random
import turtle

rgb_colours = [(245, 242, 238), (247, 238, 242), (205, 162, 112), (238, 245, 240), (142, 87, 59), (232, 236, 242), (147, 18, 27), (224, 199, 135), (51, 92, 124), (124, 158, 178), (154, 147, 67), (11, 94, 69), (141, 32, 28), (207, 87, 64), (134, 64, 68), (63, 48, 45), (50, 120, 93), (145, 177, 148), (38, 62, 75), (165, 136, 148), (63, 43, 45), (236, 169, 159), (25, 74, 96), (180, 201, 170), (185, 83, 88), (6, 77, 72), (231, 173, 178), (96, 145, 126), (35, 67, 94), (182, 191, 204)]

ernie = Turtle()
ernie.hideturtle()
ernie.penup()
turtle.colormode(255)
ernie.setheading(225)
ernie.forward(300)
ernie.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    ernie.dot(20, random.choice(rgb_colours))
    ernie.forward(50)

    if dot_count % 10 == 0:
        ernie.setheading(90)
        ernie.forward(50)
        ernie.setheading(180)
        ernie.forward(500)
        ernie.setheading(0)

screen = Screen()
screen.exitonclick()