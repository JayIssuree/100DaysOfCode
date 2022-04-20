from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snake = []
        self.head = Turtle(shape="square")
        self.head.color("white")
        self.head.pu()
        self.snake.append(self.head)
        self.add_tail()
        self.add_tail()

    def add_tail(self):
        new_tail = Turtle(shape="square")
        new_tail.color("white")
        new_tail.pu()
        old_tail = self.snake[-1]
        self.position_new_tail(old_tail, new_tail)
        self.snake.append(new_tail)

    def position_new_tail(self, old_tail, new_tail):
        heading = old_tail.heading()
        if heading == 0:
            new_tail.setposition(x=old_tail.xcor() - 20, y=old_tail.ycor())
        elif heading == 90:
            new_tail.setposition(x=old_tail.xcor(), y=old_tail.ycor() - 20)
        elif heading == 180:
            new_tail.setposition(x=old_tail.xcor() + 20, y=old_tail.ycor())
        elif heading == 270:
            new_tail.setposition(x=old_tail.xcor(), y=old_tail.ycor() + 20)

    def move(self):
        start = len(self.snake) - 1
        for seg_num in range(start, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)