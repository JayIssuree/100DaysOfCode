from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.setpos(STARTING_POSITION)
        self.shape("turtle")
        self.seth(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def levelComplete(self):
        if self.ycor() > FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            return True
        return False
    
    def check_collision(self, car):
        if self.distance(car) < 21:
            return True
        return False