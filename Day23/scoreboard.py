from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.pu()
        self.setpos(-250, 250)
        self.display_score()

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER", align="center", font=FONT)