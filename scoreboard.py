import random
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.double = random.randint(1, 5)
        self.update_score()

    def update_score(self):
        self.goto(x=0, y=250)
        self.write(f'Score: {self.score}', align="center", font=("Arial", 20, "normal"))

    def print_extra(self):
        if self.score == self.double - 1:
            self.goto(0, 0)
            self.write("EXTRA POINT", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def extra_points(self):
        if self.score == self.double:
            self.print_extra()
            new_random = random.randint(1, 25)
            capture = self.double + self.score + random.randint(self.double, self.score + new_random)
            self.score = self.score + self.double
            self.double = self.double + capture
            self.clear()
            self.update_score()