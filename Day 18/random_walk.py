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

colors =['red', 'blue', 'brown', 'yellow', 'indianred', 'cyan3', 'cyan1', 'green1', 'green4', 'grey']
sides = [90, 0, 180, 270]

tim.pensize(5)
tim.speed(0)
random_direction = random.choice(sides)
for direction in range(150):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random_direction)
    tim.right(random.choice(sides))
    tim.left(random.choice(sides))

screen= Screen()
screen.exitonclick() 
    