from turtle import Turtle, Screen

wn = Screen()


class Paddle(Turtle):
    def __init__(self, intial_x):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.setheading(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(intial_x, 0)

    def up(self):
        if self.ycor() < 241:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.sety(new_y)
