import turtle
from turtle import Turtle


class Hangman:
    def __init__(self):
        self.turtle_object = Turtle()
        self.border_length = 350
        self.stage_length = 40
        self.radius = 30
        self.turtle_object.ht()

    def draw_frames(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-170, -150)
        self.turtle_object.pendown()
        self.turtle_object.left(90)
        self.turtle_object.forward(self.border_length)
        self.turtle_object.right(90)
        self.turtle_object.forward(self.border_length)
        self.turtle_object.right(90)
        self.turtle_object.forward(self.border_length)
        self.turtle_object.right(90)
        self.turtle_object.forward(self.border_length)
        self.turtle_object.penup()
        self.turtle_object.goto(-100, -50)
        self.turtle_object.pendown()
        self.turtle_object.begin_fill()
        self.turtle_object.fillcolor("red")
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.left(90)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.left(90)
        self.turtle_object.forward(self.stage_length + self.stage_length)
        self.turtle_object.left(90)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.left(90)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.end_fill()
        self.turtle_object.pensize(5)
        self.turtle_object.right(90)
        self.turtle_object.forward(self.border_length / 2 + self.stage_length)
        self.turtle_object.right(90)
        self.turtle_object.forward(self.stage_length + self.stage_length)
        self.turtle_object.right(90)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.ht()

    def draw_head(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-50, 94)
        self.turtle_object.pendown()
        self.turtle_object.color("blue")
        self.turtle_object.begin_fill()
        self.turtle_object.fillcolor("yellow")
        self.turtle_object.pensize(3)
        self.turtle_object.circle(self.radius)
        self.turtle_object.end_fill()
        self.turtle_object.penup()
        self.turtle_object.goto(-40, 92)
        self.turtle_object.pendown()
        self.turtle_object.begin_fill()
        self.turtle_object.fillcolor("black")
        self.turtle_object.pensize(2)
        self.turtle_object.circle(4)
        self.turtle_object.end_fill()
        self.turtle_object.penup()
        self.turtle_object.goto(-10, 92)
        self.turtle_object.pendown()
        self.turtle_object.begin_fill()
        self.turtle_object.fillcolor("black")
        self.turtle_object.pensize(2)
        self.turtle_object.circle(4)
        self.turtle_object.end_fill()
        self.turtle_object.ht()

    def draw_body(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-20, 65)
        self.turtle_object.pendown()
        self.turtle_object.forward(self.stage_length + self.stage_length)
        self.turtle_object.ht()

    def draw_left_hand(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-20, 45)
        self.turtle_object.pendown()
        self.turtle_object.left(44)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.left(80)
        self.turtle_object.forward(self.stage_length / 2)
        self.turtle_object.ht()

    def draw_right_hand(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-20, 45)
        self.turtle_object.pendown()
        self.turtle_object.right(160)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.right(80)
        self.turtle_object.forward(self.stage_length / 2)
        self.turtle_object.ht()

    def draw_left_leg(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-20, -15)
        self.turtle_object.pendown()
        self.turtle_object.left(170)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.left(80)
        self.turtle_object.forward(self.stage_length / 2)
        self.turtle_object.ht()

    def draw_right_leg(self):
        self.turtle_object.penup()
        self.turtle_object.goto(-20, -15)
        self.turtle_object.pendown()
        self.turtle_object.right(180)
        self.turtle_object.forward(self.stage_length)
        self.turtle_object.right(80)
        self.turtle_object.forward(self.stage_length / 2)
        # turtle.done()
        self.turtle_object.ht()

    def set_default(self):
        self.turtle_object.reset()
        turtle.done()
