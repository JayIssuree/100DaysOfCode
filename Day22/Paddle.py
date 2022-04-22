from turtle import Turtle
MOVE_DISTANCE = 40


class Paddle(Turtle):

    def __init__(self, xcor, ycor=0):
        super().__init__()
        self.pu()
        self.speed("fastest")
        self.seth(90)
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setpos(x=xcor, y=ycor)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)