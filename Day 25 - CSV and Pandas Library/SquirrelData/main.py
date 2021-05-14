# count the number of squirells based on color
# make a df of it.

import pandas as pd

content = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# content = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"]
# create a dataframe with one column
# color_series = pd.DataFrame(content["Primary Fur Color"])
count_series = pd.Series(content["Primary Fur Color"]).value_counts()

print(count_series.Gray)
my_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [count_series.Gray, count_series.Cinnamon, count_series.Black]
}

df = pd.DataFrame(my_dict)

df.to_csv("final.csv")

# Alternate
# Central Park Squirrel Data Analysis
# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
