import time
from globals import WIDTH, HEIGHT
import turtle as tt
from paddle import Paddle
from ball import Ball
from brick import BrickManager
import random
import math
BG_COLOR = '#211832'  # 561530

# initialize the screen
wn = tt.Screen()

# remove the white highlight around the window
canvas = wn.getcanvas()
canvas.config(bd=0, highlightthickness=0)
canvas.config(bg=BG_COLOR)

# setup the wn
wn.setup(width=WIDTH, height=HEIGHT)
wn.bgcolor(BG_COLOR)
wn.title('Atari\'s Breakout(a sim)')

wn.tracer(0)

paddle = Paddle()
ball = Ball()
bricks = BrickManager()
keys_pressed = set()

def move_paddle():
    current_x = paddle.pos()[0]
    if "Left" in keys_pressed and current_x > -300.0:
        print(paddle.pos())
        paddle.backward(100)
    elif "Right" in keys_pressed and current_x < 300.0:
        print(paddle.pos())
        paddle.forward(100)
    wn.update()
    wn.ontimer(move_paddle, 50)

def key_down(key):
    keys_pressed.add(key)
def key_up(key):
    keys_pressed.discard(key)

wn.listen()
wn.onkeypress(lambda: key_down('Left'), 'Left')
wn.onkeyrelease(lambda: key_up('Left'), 'Left')

wn.onkeypress(lambda: key_down('Right'), 'Right')
wn.onkeyrelease(lambda: key_up('Right'), 'Right')
move_paddle()

# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
num_of_rows = 5

for i in range(num_of_rows):
    wn.update()
    bricks.create_bricks(i+1)


def handle_click(x, y):
    print(f"Clicked at coordinates: ({x}, {y})")
    # paddle.goto(x, y)

wn.onscreenclick(handle_click)

wn.mainloop()
