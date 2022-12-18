import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)