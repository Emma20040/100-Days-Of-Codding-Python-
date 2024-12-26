from turtle import Turtle, Screen

tim = Turtle()
screen= Screen()

def move():
    tim.forward(20)

screen.listen()
screen.onkey(key="space", fun= move)

screen.exitonclick()