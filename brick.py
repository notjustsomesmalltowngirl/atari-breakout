from turtle import Turtle
import random
import time
import math
from globals import WIDTH, HEIGHT

WIDTHS = [4, 5, 6, 7]
COLORS = [
    '#9E1C60', '#F5DAA7', '#05339C',
    '#9B5DE0', '#0046FF', '#D97D55', '#637AB9',
    '#FFBBE1', '#DD7BDF', '#BF092F', '#FF3F7F',
    '#CBCBCB', '#9B5DE0', '#B4DEBD', '#696FC7',
    '#5D866C', '#F2AEBB', '#006A67', '#96A78D'
]


class BrickManager(Turtle):
    def __init__(self):
        super().__init__()
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.all_bricks = []
        self.num_of_rows = 5
        self.hideturtle()
        self.all_pos = self.generate_brick_positions()
        self.brick_pos = {}

    def generate_brick_positions(self):

        self.stretch_len = random.randint(5, 8)
        self.stretch_height = random.randint(1, 2)

        self.brick_height_pixel = self.stretch_height * 10
        self.brick_width_pixel = 20 * self.stretch_len

        self.init_x_cord = -(self.screen_width - self.brick_width_pixel) // 2
        self.init_y_coord = (self.screen_height / 2) - self.brick_height_pixel

        self.spacing = random.randint(4, 7)

        all_rows = {
            i + 1: [
                (
                    self.init_x_cord + (self.brick_width_pixel + self.spacing) * j,
                    self.init_y_coord - i * (2 * self.brick_height_pixel + self.spacing)
                )
                for j in range(math.ceil(self.screen_width / self.brick_width_pixel))
            ]
            for i in range(self.num_of_rows)
        }
        return all_rows
    def create_bricks(self, row):
        for x, y in self.all_pos[row]:
            self.brick_pos[row] = []
            new_brick = Turtle("square")

            new_brick.shapesize(stretch_wid=self.stretch_height, stretch_len=self.stretch_len)
            new_brick.penup()
            new_brick.color(random.choice(COLORS))
            new_brick.goto(x, y)
            self.all_bricks.append(new_brick)


