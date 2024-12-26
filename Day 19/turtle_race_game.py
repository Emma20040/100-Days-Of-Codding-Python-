from turtle import Turtle, Screen
import random

screen= Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color ")
print(user_bet)
screen.listen()

start_race= False
colors= ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates =[-130, -90, -40, 10, 60, 100]
all_turtles =[]


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -235, y= y_coordinates[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    start_race= True

while start_race:
    for turtle in all_turtles:
        if turtle.xcor() >225:
            start_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win, the {winner} turtle is the winner ")
            else:
                print(f"You loss!!, the {winner} turtle is the winner ")
        random_distance= random.randint(1, 10)
        turtle.forward(random_distance)


# tom = Turtle(shape= "turtle")
# tom.color('orange')
# tom.penup()
# tom.goto(x= -235, y= -90)

# jerry = Turtle(shape= "turtle")
# jerry.color('yellow')
# jerry.penup()
# jerry.goto(x= -235, y= -40)

# mark = Turtle(shape= "turtle")
# mark.color('green')
# mark.penup()
# mark.goto(x= -235, y= 10)

# timmy = Turtle(shape= "turtle")
# timmy.color('blue')
# timmy.penup()
# timmy.goto(x= -235, y= 60)

# tommy = Turtle(shape= "turtle")
# tommy.color('purple')
# tommy.penup()
# tommy.goto(x= -235, y= 110)

screen.exitonclick()