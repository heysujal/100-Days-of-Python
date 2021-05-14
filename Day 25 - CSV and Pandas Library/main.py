# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#
# print(data_list)

# import csv

# with open("weather_data.csv") as data_file:
#     data = (csv.reader(data_file))
#     temperatures = []
#     # next(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row,row[0])
#     print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# get data in a row
# monday = data[data.day=="Monday"]
# monday_temp  = int(monday.temp)
# temp_in_farenheit = (monday_temp*9)/5 + 32
# print(temp_in_farenheit)
# create a dataframe from a dict

my_dict = {
    "name": ["Sujal", "Nitin", "Abhinav"],
    "scores": [90, 100, 99]
}
# print(my_dict)
df = pandas.DataFrame(my_dict)
print(df)
df.to_csv("newdata.csv")
