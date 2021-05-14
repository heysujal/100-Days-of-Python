import turtle

import pandas as pd

# screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

answer = turtle.textinput(title="Guess the state", prompt="What's another state's name? ").title()
# print(answer)

data = pd.read_csv("50_states.csv")
names_list = data.state.to_list()

# flag = 0
for name in names_list:
    if name == answer:
        # flag = 1
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        # desired_row = data.loc[data['state'] == answer]

        desired_row_new = data[data.state == answer]
        # How to print x and y from this row?
        print(desired_row)
        print(desired_row_new)
        # print(type(desired_row.x))
        # print(desired_row.y)
        # # x_cor = desired_row.x
        # y_cor = desired_row.y
        # print(x_cor,y_cor)

        # new_turtle.goto(desired_row.x,desired_row.y)
        # new_turtle.write(f"{answer}")
        break

# list_of_coordinates = list(zip(data.x, data.y))
# print(list_of_coordinates)
# x_list = data.x
# print(x_list)

# print(names_list)
# print(data)


turtle.mainloop()
# screen.exitonclick()
