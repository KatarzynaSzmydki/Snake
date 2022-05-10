

from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.find_food()

    def find_food(self):
        food = Turtle()
        food.color("blue")
        food.penup()
        food.shape('circle')
        food.shapesize(0.5,0.5,0.5)
        coord_x = random.randint(-300,300)
        coord_y = random.randint(-300, 300)
        food.setposition(coord_x, coord_y)
        return food


