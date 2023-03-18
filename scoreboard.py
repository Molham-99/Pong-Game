from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()

    def score_1(self):
        self.write(f"{self.score1}     {self.score2}", move=False, align="center", font= ("Arial", 30, "normal"))

    def increase_score1(self):
        self.clear()
        self.score1 += 1

    def increase_score2(self):
        self.clear()
        self.score2 += 1
