from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time 

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detecting collision with the upper wall
    if ball.ycor() >280 or   ball.ycor() <-280:
        ball.bounce_y()
    
    # detecting collision with the right and left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if right misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
    

screen.exitonclick()









