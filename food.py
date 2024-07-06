from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.shapesize(0.7)
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        randomx = random.randint(-200, 200)
        randomy = random.randint(-200, 200)
        self.goto(randomx, randomy)