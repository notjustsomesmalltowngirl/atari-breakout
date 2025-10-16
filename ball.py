from turtle import Turtle
from globals import WIDTH, HEIGHT

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.turtlesize(stretch_wid=0.7)
        # self.penup()
        self.speed(1)
        self.color('#BF092F')
        self.setpos(0, -((HEIGHT/2)-25))

    def move(self, x_position, y_position):
        self.goto(x_position, y_position)
        # self.goto(0, -((HEIGHT/2)-25))
        # print(self.pos())