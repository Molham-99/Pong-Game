from turtle import Turtle, Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time
paddle = Paddles()
turtle = Turtle()
ball = Ball()
scoreboard = Scoreboard()
turtle.color("white")
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=630)
screen.title("Pong Game Created By Molham")
screen.tracer(0)
turtle.hideturtle()
turtle.penup()
turtle.setposition(0, -300)
turtle.left(90)
screen.listen()
for x in range(31):
    turtle.pendown()
    turtle.pensize(3)
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
screen.onkey(fun=paddle.up_paddle_1, key="w")
screen.onkey(fun=paddle.down_paddle_1, key="s")
screen.onkey(fun=paddle.up_paddle_2, key="Up")
screen.onkey(fun=paddle.down_paddle_2, key="Down")
game_is_on = True
while game_is_on:
    screen.update()
    scoreboard.score_1()
    paddle.move_paddle_1()
    paddle.move_paddle_2()
    ball.move_ball()
    time.sleep(0.1)
    if ball.ball.distance(paddle.paddle_1[0]) < 30 and ball.ball.heading() == 135:
        ball.ball.setheading(45)
    elif ball.ball.distance(paddle.paddle_1[0]) < 30 and ball.ball.heading() == 225:
        ball.ball.setheading(315)
    elif ball.ball.distance(paddle.paddle_2[0]) < 30 and ball.ball.heading() == 315:
        ball.ball.setheading(225)
    elif ball.ball.distance(paddle.paddle_2[0]) < 30 and ball.ball.heading() == 45:
        ball.ball.setheading(135)
    elif ball.ball.xcor() >= 500:
        scoreboard.increase_score1()
        ball.restart_game()
        ball.ball.setheading(225)
    elif ball.ball.xcor() <= -500:
        scoreboard.increase_score2()
        ball.restart_game()
        ball.ball.setheading(315)
    ball.speed += 0.05





screen.exitonclick()