import time
from globals import WIDTH, HEIGHT
import turtle as tt
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from brick import BrickManager
import random

# --- EVENT FUNCTIONS ---
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
score_board = ScoreBoard()

bricks = BrickManager()

X_LIM = WIDTH/2-100

def move_paddle_with_mouse(event):
    x = event.x - wn.window_width() / 2
    paddle.setx(x)

keys_pressed = set()
def key_down(key):
    keys_pressed.add(key)
def key_up(key):
    keys_pressed.discard(key)
def move_paddle_with_keys():
    current_x = paddle.pos()[0]
    if "Left" in keys_pressed and current_x >= -(X_LIM+10):
        paddle.backward(100)
    elif "Right" in keys_pressed and current_x <= (X_LIM+10):
        paddle.forward(100)
    wn.update()
    wn.ontimer(move_paddle_with_keys, 50)

# EVENT BINDING
canvas.bind("<Motion>", move_paddle_with_mouse)
wn.listen()
wn.onkeypress(lambda: key_down('Left'), 'Left')
wn.onkeyrelease(lambda: key_up('Left'), 'Left')

wn.onkeypress(lambda: key_down('Right'), 'Right')
wn.onkeyrelease(lambda: key_up('Right'), 'Right')
move_paddle_with_keys()

for i in range(bricks.num_of_rows):
    wn.update()
    bricks.create_bricks(i + 1)


while True:
    score_board.display_lives()
    # score_board.display_level()
    distances = [20, 50, 30, 40, 50, 60]
    time.sleep(ball.move_speed)
    wn.update()
    ball.move()
    ball_x_position, ball_y_position = ball.position()

    # check if the ball is hitting the side walls
    if ball_x_position < - (X_LIM + 100) or ball_x_position > (X_LIM + 100):
        if ball_x_position < 0: ball.forward(random.choice(distances))
        # else move it backward
        else: ball.backward(random.choice(distances))
        ball.bounce_x()

    # check if the ball is hitting top wall
    if ball_y_position >= 230:
        ball.sety(229)
        print("Ball in y positive danger zone.") # TODO: bug gets stuck here sometimes
        # ball.backward(100)
        ball.bounce_y()

    # if the ball hits the bottom wall,
    if ball_y_position <= -230:
        # check if it collides with the paddle
        if ball.distance(paddle) <= 60:
            ball.bounce_y()
        else:
            ball.reset_position()
            score_board.decrease_lives()
            if score_board.lives == 0:
                ball.hideturtle()
                paddle.hideturtle()
                score_board.display_score(f'Game over: You hit {score_board.score} bricks.')
                break
    # loop through all bricks
    for brick in bricks.all_bricks:
        # check if the ball has moved close to a brick, if yes
        if brick.isvisible() and brick.distance(ball) < 80:
            brick.hideturtle() # remove the brick
            if ball.move_speed >= 0.01:
                ball.move_speed -= 0.002
            score_board.update_score()
            ball.bounce_y() # make the ball move in the opposite y direction
            ball.forward(random.choice(distances)) # move it forward
            break
    no_visible_brick = True
    for brick in bricks.all_bricks:  # check if all bricks are gone
        if brick.isvisible():
            no_visible_brick = False
            break
    if no_visible_brick:
        score_board.display_score(f'You hit all {score_board.score} bricks.')
        ball.hideturtle()
        paddle.hideturtle()
        break

wn.mainloop()
