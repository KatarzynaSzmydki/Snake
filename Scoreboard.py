FILE = 'highest_score.txt'


from Snake import Snake
from Food import Food
import random
from turtle import Turtle
from os.path import exists

class Scoreboard(Snake):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.food = Food.find_food(self)
        self.scoreboard = Turtle()
        self.highest_score = 0
        self.read_highest_score()
        self.print_score()


    def read_highest_score(self):
        if exists(FILE):
            with open(FILE, 'r') as f:
                self.highest_score = int(f.read())



    def count_score(self):

        # print('distance', self.snakes_head.distance(self.food))
        # print(self.snakes_head.position(), self.food.position())

        if self.snakes_head.distance(self.food.position()) < 20:
            print('distance', self.snakes_head.distance(self.food))
            x = self.snakes[len(self.snakes) - 1].xcor()-20
            y = self.snakes[len(self.snakes) - 1].ycor()
            self.score += 1
            print(f'Snake is growing! Your score: {self.score}')
            self.create_snake(1, x, y)
            self.food.setposition(random.randint(-300, 300), random.randint(-300, 300))
            self.scoreboard.clear()
            self.print_score()


    def print_score(self):
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(0, 270)
        self.scoreboard.pencolor("white")
        self.scoreboard.write(f'Score: {self.score} Highest Score: {self.highest_score}', move=False, align='center', font=("Arial", 12, "normal"))


    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.score = 0
            with open(FILE, 'w') as f:
                f.write(str(self.highest_score))

