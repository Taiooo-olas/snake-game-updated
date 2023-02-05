from turtle import Turtle
import random
import time


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(x=random_x, y=random_y)

    def special_ball(self):
        self.color("yellow", "red")
        # if code hangs: comment out While true statement and use static (Self.color)
        # while True:
        #     color = ["yellow", "red", "white", "blue"]
        #     for loop in color:
        #         self.color(loop)
        #         time.sleep(0.5)
