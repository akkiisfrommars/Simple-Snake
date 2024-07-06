import turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.number_of_pauses = 3

    def create_snake(self):
        for index, position in enumerate(STARTING_POSITIONS):
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            if index == 0:
                new_segment.color("grey")
            else:
                new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_segment(self):
        n_seg = turtle.Turtle()
        n_seg.shape("square")
        n_seg.color("white")
        n_seg.penup()
        n_seg.goto(self.segments[-1].position())
        self.segments.append(n_seg)

    def delete_segment(self):
        if len(self.segments) > 3:
            segment_to_delete = self.segments.pop()
            segment_to_delete.hideturtle()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def pause(self):
        if self.number_of_pauses > 0:
            self.number_of_pauses -= 1
            time.sleep(5)
