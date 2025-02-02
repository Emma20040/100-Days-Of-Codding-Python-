from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# color = random.choice(COLORS)


class CarManager:
    def __init__(self):
        
        self.all_cars =[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
       random_chance = random.randint(1, 6)
       if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=0.6)

            x_coordinate =280
            y_coordinate= random.randint(-250, 250)
            new_car.goto(x_coordinate, y_coordinate)
            
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    
