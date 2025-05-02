import turtle as t
import random
from turtle import Screen
shape= t.Turtle()

colors =['red', 'blue', 'brown', 'yellow', 'indianred', 'cyan3', 'cyan1', 'green1', 'green4', 'grey']
def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for i in range(number_of_sides):
        shape.forward(90)
        shape.right(angle)

for shape_number_side in range(3, 11):
    shape.color(random.choice(colors))
    draw_shape(shape_number_side)

screen= Screen()
screen.exitonclick() 