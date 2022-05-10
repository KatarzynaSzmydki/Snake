
from turtle import Screen
import turtle as t
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
t.penup()


snake = Snake()
food = Food.food()

screen.listen()
screen.ontimer(snake.play, 75)
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')

Snake.play()
screen.mainloop()
# screen.exitonclick()