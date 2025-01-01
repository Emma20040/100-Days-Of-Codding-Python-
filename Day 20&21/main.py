from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time 


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detecting collision withe the wall
    if snake.head.xcor() >295 or  snake.head.xcor() <-295 or  snake.head.ycor() >295 or  snake.head.ycor() <-295:
       scoreboard.reset()
       
       snake.reset()

    # detecting collision with tail
    for segment in snake.segments:
       if segment == snake.head:
          pass
       elif snake.head.distance(segment)<10:
         scoreboard.reset()
         
         snake.reset()


screen.exitonclick()









# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)
