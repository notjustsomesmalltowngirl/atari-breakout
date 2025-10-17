from turtle import Turtle
from globals import HEIGHT

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(0)
        self.turtlesize(stretch_wid=0.5, stretch_len=5)
        self.color('#FCF9EA')
        self.setpos(0, -((HEIGHT/2)-10))

