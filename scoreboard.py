from turtle import Turtle
from globals import HEIGHT, WIDTH
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 5
        # self.level = 1
        self.color('white')

        # with open("data.txt") as book:
        #     self.high_score = int(book.read())
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.score += 1

    def decrease_lives(self):
        self.lives -= 1

    def display_lives(self):
        self.clear()
        self.goto(((WIDTH/2)-200), -(HEIGHT-250))
        self.write(f'Lives left: {self.lives}', font=FONT)
        if self.lives <=2:
            self.color('#BF092F')

    def display_score(self, text):
        # self.clear()
        self.color('white')
        self.goto(0, 0)

        self.write(text, font=FONT)
    # def display_level(self):
    #     # self.clear()
    #     self.goto(-((WIDTH / 2) - 200), -(HEIGHT - 250))
    #     self.write(f'Level: {self.level}', font=FONT)