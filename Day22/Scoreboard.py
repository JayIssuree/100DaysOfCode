import imp
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()

    def increment_lscore(self):
        self.lscore += 1
        self.update_scoreboard()

    def increment_rscore(self):
        self.rscore += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))