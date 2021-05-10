import turtle
import random


turtle.colormode(255)
tim = turtle.Turtle()
tim.speed('fastest')
# turtle.speed('fastest')
# tim.pensize(10)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb


angle = 0



for _ in range(360//5):
    tim.color(random_color())
    tim.circle(100)
    # tim.forward(50)
    tim.setheading(angle)
    angle += 5
