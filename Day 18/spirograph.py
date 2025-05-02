import turtle as t
from turtle import Screen
import random

tim= t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =(r, g,b )
    return random_color

tim.speed(0)

for i in range(100):
    tim.color(random_color())
    tim.circle(120)
    # tim.left(5)
    tim.setheading(tim.heading() + 10)
    

screen= Screen()
screen.exitonclick() 
    