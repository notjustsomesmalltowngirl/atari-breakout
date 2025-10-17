import random
import time
from turtle import Turtle
from globals import HEIGHT

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.turtlesize(stretch_wid=0.7)
        self.penup()
        self.score = 0
        self.x_move =  random.choice([-10, 10])
        self.y_move = 10
        self.move_speed = 0.04
        self.num_of_resets = 0
        self.color('#BF092F')
        self.setpos(0, -((HEIGHT/2)-25))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #  so that when move is called in the while it does it the reverse with the new_y
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()

