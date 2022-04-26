from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(-27, 280)
        self.score = 0
        self.high_score = self.retrieve_highscore()
        self.penup()
        self.color("white")
        self.display_score()

    def retrieve_highscore(self):
        with open("Data.txt") as file:
            data = file.read()
            return int(data)

    def update_highscore(self):
        with open("Data.txt", "w") as file:
            file.write(str(self.score))

    def increment(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=50, align="center")

    def update(self):
        self.increment()
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.score = 0
        self.display_score()