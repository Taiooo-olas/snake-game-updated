from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_RIGHT = 0
MOVE_DOWN = 270
MOVE_LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_link(position)

    def move_snake(self):
        for link in range (len(self.segments)-1, 0, -1):
            number_x = self.segments[link - 1].xcor()
            number_y = self.segments[link - 1].ycor()
            self.segments[link].goto(number_x, number_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_link(self.segments[-1].position())

    def add_link(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)

    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)