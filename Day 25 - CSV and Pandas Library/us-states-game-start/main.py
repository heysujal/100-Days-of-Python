import turtle

import pandas as pd

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
names_list = data.state.to_list()
done = 0

while len(names_list) > 0:

    flag = 0
    answer = turtle.textinput(title="Guess the state", prompt=f"What's another state's name?({done}/50) ").title()
    if answer == "Exit":
        break
    if answer in names_list:
        flag = 1
        done += 1
        desired_row = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(desired_row.x), int(desired_row.y))
        t.write(answer)
        # t.write(desired_row.state.item())
    if flag:
        names_list.remove(answer)

if len(names_list):
    unguessed = pd.DataFrame(names_list)
    unguessed.to_csv('answers_left.csv')

# turtle.mainloop() to stop the screen
