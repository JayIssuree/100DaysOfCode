from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(-27, 280)
        self.score = 0
        self.penup()
        self.color("white")
        self.display_score()

    def increment(self):
        self.score += 1

    def display_score(self):
        self.write(f"Score: {self.score}", font=50)

    def update(self):
        self.clear()
        self.increment()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!")