from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.color("green")
        self.ball.penup()
        self.ball.setheading(45)
        self.speed = 10

    def move_ball(self):
        self.ball.forward(self.speed)
        if self.ball.ycor() >= 290:
            if self.ball.heading() == 45:
                self.ball.setheading(315)
            elif self.ball.heading() == 135:
                self.ball.setheading(225)
        elif self.ball.ycor() <= -290:
            if self.ball.heading() == 225:
                self.ball.setheading(135)
            elif self.ball.heading() == 315:
                self.ball.setheading(45)

    def restart_game(self):
        self.ball.penup()
        self.ball.goto(0,0)
        self.speed = 10

