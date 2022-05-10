

from turtle import Turtle


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake(3,0,0)
        self.snakes_head = self.snakes[0]
        self.game_is_on = True
        self.print = Turtle()




    def create_snake(self, size, x, y):
        for i in range(size):
            snake = Turtle()
            snake.shape("square")
            snake.penup()
            if len(self.snakes)>0:
                snake.goto(x,y)
            else:
                snake.setposition(-20 + i*20, 0)
            snake.color("white")
            self.snakes.append(snake)



    def left(self):
        self.snakes_head.setheading(180)

    def right(self):
        self.snakes_head.setheading(0)

    def up(self):
        self.snakes_head.setheading(90)

    def down(self):
        self.snakes_head.setheading(270)


    def wall(self):
        if self.snakes_head.xcor() >= 300 or self.snakes_head.xcor() <= -300 or self.snakes_head.ycor() >= 300 or self.snakes_head.ycor() <= -300:
            self.game_is_on = False
        else:
            self.game_is_on = True


    def collision(self):
        for snake in range(1, len(self.snakes) - 1):
            # if (self.snakes_head.xcor() == self.snakes[snake].xcor() and self.snakes_head.ycor() == self.snakes[snake].ycor()):
            if self.snakes_head.distance(self.snakes[snake].position()) < 10:
                self.game_is_on = False



    def print_text(self):
        self.print.hideturtle()
        self.print.penup()
        self.print.pencolor("white")
        self.print.goto(0, 0)
        self.print.write('GAME OVER', move=False, align='center', font=("Arial", 12, "normal"))


    def play(self):

        self.wall()
        self.collision()
        if self.game_is_on == False:
            print('GAME OVER')
            for snake in range(0,len(self.snakes) - 1, 1):
                new_x = self.snakes[snake + 1].xcor()
                new_y = self.snakes[snake + 1].ycor()
                self.snakes[snake].goto(new_x, new_y)
            self.print_text()

        else:

            for snake in range(len(self.snakes) - 1, 0, -1):
                new_x = self.snakes[snake - 1].xcor()
                new_y = self.snakes[snake - 1].ycor()
                self.snakes[snake].goto(new_x, new_y)
            self.snakes_head.forward(20)





