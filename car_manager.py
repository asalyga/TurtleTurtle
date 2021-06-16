from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        chance = randint(1, 10)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_left(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
