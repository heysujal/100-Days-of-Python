from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "yellow", "orange", "blue", "purple"]
y_offset = 0
all_turtles = []
winner_color = ""

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-80 + y_offset)
    new_turtle.speed('fastest')
    all_turtles.append(new_turtle)

    y_offset += 30

# start off the race
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)
        if (turtle.xcor()) >= 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            break

if user_bet == winner_color:
    print("You win!")
else:
    print("You lose!")
print(f"The winner is {winner_color} turtle")

screen.exitonclick()
