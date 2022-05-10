

from turtle import Turtle, Screen
import turtle as t
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
t.penup()


snakes = []
def create_snake(size, x, y):
    for i in range(size):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        if len(snakes)>0:
            snake.goto(x,y)
        else:
            snake.setposition(-20 + i*20, 0)
        snake.color("white")
        snakes.append(snake)



def left():
    snakes[0].setheading(180)

def right():
    snakes[0].setheading(0)

def up():
    snakes[0].setheading(90)

def down():
    snakes[0].setheading(270)


def wall():
    if snakes[0].xcor() >= 300:
        return True
    elif snakes[0].xcor() <= -300:
        return True
    elif snakes[0].ycor() >= 300:
        return True
    elif snakes[0].ycor() <= -300:
        return True
    else:
        return False


def text_xy():
    t.penup()
    t.write("GAME OVER!",True, align="center")



def food():
    food = Turtle()
    food.color("blue")
    food.penup()
    food.shape('circle')
    food.shapesize(1,1,1)
    coord_x = random.randint(-300,300)
    coord_y = random.randint(-300, 300)
    food.setposition(coord_x, coord_y)
    return food



def play():

    if wall():
        print('GAME OVER')
        for snake in range(0,len(snakes) - 1, 1):
            new_x = snakes[snake + 1].xcor()
            new_y = snakes[snake + 1].ycor()
            snakes[snake].goto(new_x, new_y)
            snakes[snake].goto(new_x,new_y)
        text_xy()
        screen.title("GAME OVER!")
        # t.bye()

    else:

        for snake in range(len(snakes) - 1, 0, -1):
            new_x = snakes[snake - 1].xcor()
            new_y = snakes[snake - 1].ycor()
            snakes[snake].goto(new_x, new_y)
        snakes[0].forward(20)
        screen.ontimer(play, 50)
        screen.onkey(fun=left, key='Left')
        screen.onkey(fun=right, key='Right')
        screen.onkey(fun=up, key='Up')
        screen.onkey(fun=down, key='Down')

        # print(snakes[0].position(), food.position())

        if snakes[0].distance(food.position()) < 10:
            print('distance', snakes[0].distance(food))
            x = snakes[len(snakes) - 1].xcor()-20
            y = snakes[len(snakes) - 1].ycor()
            print('Snake is growing!')
            create_snake(1, x, y)
            food.setposition(random.randint(-300, 300), random.randint(-300, 300))





create_snake(3, 0, 0)
food = food()
screen.listen()
play()
screen.mainloop()
# screen.exitonclick()