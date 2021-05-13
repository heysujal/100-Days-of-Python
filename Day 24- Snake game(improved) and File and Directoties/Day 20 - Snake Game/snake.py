from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        # self.head = self.all_turtles[0]

        # for turtle_index in range(0,3):

    def create_snake(self):
        # self.head = self.all_turtles[0]
        for position in starting_positions:
            self.add_segment(position)
        self.head = self.all_turtles[0]

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def extend(self):
        self.add_segment(starting_positions[-1])

    def move(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.all_turtles:
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        Turtle().clear()
        self.create_snake()
