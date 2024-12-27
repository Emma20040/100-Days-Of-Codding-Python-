from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP =90
DOWN = 270
LEFT = 180
RIGHT = 0

screen =Screen()
# segments =[]
class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment= Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)


    def move(self):
        for segment_number  in range(len(self.segments)-1, 0, -1):
            xcoordinate =self.segments[segment_number-1].xcor()
            ycoordinate= self.segments[segment_number-1].ycor()
            self.segments[segment_number].goto(xcoordinate, ycoordinate)
        self.segments[0].forward(DISTANCE)
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
 
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
 

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
 

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 
 
