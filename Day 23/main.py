import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player= Player()
car = CarManager()
scoreboard = Scoreboard()
tim = Turtle()
tim.hideturtle()


screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    

    # detect colision with car
    for moving_car in car.all_cars:
        if moving_car.distance(player) <25:
            tim.write('Game over', align='center', font=("Courier", 15, "normal"))
            tim.goto(0,0)
            game_is_on= False

    
    # dtecting when player reaches the top of the screen
    if player.ycor()== 290:
        scoreboard.point()
        player.goto(0,-290)
        car.level_up()
        


screen.exitonclick()