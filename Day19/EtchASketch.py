from turtle import Turtle, Screen

ernie = Turtle()
screen = Screen()

def move_forwards():
    ernie.forward(10)

def move_backwards():
    ernie.backward(10)

def turn_clockwise():
    ernie.right(15)

def turn_anticlockwise():
    ernie.left(15)    

def clear_screen():
    ernie.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()