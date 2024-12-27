from turtle import Turtle, Screen
import time 
from snake import Snake

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position =[(0, 0), (-20, 0), (-40, 0)]
segments =[]

for position in starting_position:
    new_segment= Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    for segment_number  in range(len(segments)-1, 0, -1):
        xcoordinate =segments[segment_number-1].xcor()
        ycoordinate= segments[segment_number-1].ycor()
        segments[segment_number].goto(xcoordinate, ycoordinate)
    segments[0].forward(20)
        











# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

screen.exitonclick()