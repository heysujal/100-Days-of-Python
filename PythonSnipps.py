# import all at once
from turtle import *

print("hello world"[0])
# underscores are ignored
mystery = 734_529.678
print(mystery)

score = 0
heigth = 2.15
isWinning = True

# F string
print(f"Your score is {score}")

# random numbers
# produces a number including 0 and 100
import random

# generates random interger
random.randint(0, 100)
# Returns the next random floating point number between [0.0 to 1.0)
random.random()
# Random
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
print(random.choice(a))
# Inbuilt python functions
sum(a)
len(a)
max(a)
min(a)
# append and add in lists
fruits = []

fruits += "orange"

print(fruits)
# ['o', 'r', 'a', 'n', 'g', 'e']

# Importing module
# or
from other_python_pile import word_list


# Keyword Argument
def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"Your location is {location}")


greet_with_name(location="Delhi", name="Sujal")

# How to get index and the element itself without using index()
for i in range(len(word_list):
    letter = word_list[i]

# Strings in python are immutable

# Dictionaries
# Create an empty dictionary

my_dict = {}
# adding new items to dictionary
my_dict["Loop"] = "An action of doing something over and over again"

# looping through a dictionary
for key in my_dict:
    print(key)
print(my_dict[key])

#######################################

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

travel_log[0] = "Sujal"  # Valid
print(travel_log[0])  # can produce error if key not found i.e. if 0 is not any key

# Scope
gamelevel = 3
enemies = ["skeleton", "zombie", "alien"]

if gamelevel < 5:
    new_enemy = enemies[0]

print(new_enemy)  # valid
# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.
# scope with function
gamelevel = 3
enemies = ["skeleton", "zombie", "alien"]
# function creates a local scope.


def fun():
    if gamelevel < 5:
        new_enemy = enemies[0]
    # print(new_enemy)  #Valid


fun()
print(new_enemy)  # Invalid

# Using global variables can lead to bugs
# they should be used only for making global constants


# This is valid code even if we dont pass enemies as argument
enemies = 1


def inc_enemy():
    print(f"enemy is {enemies} ")
    return enemies + 100


print(inc_enemy())


# the point being we cannot modify global variable inside a function


# Making Class
class Sujal:
    pass

    # Constructor
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0


# Without constructor
user1 = Sujal()
# adding attributes
user1.id = "101"

user1 = Sujal("sujal", "001")


# example2
class Sujal:
    pass

    def __init__(self, id, username):
        self.id = id
        self.username = username


user1 = Sujal(54, "heysujal")
print(user1)
print(user1.id)
print(user1.username)

# Creating multiple objects from same class
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    # new_turtle.penup()
    # new_turtle.color(colors[turtle_index])
    # new_turtle.goto(x=-230, y=-80 + y_offset)
    # new_turtle.speed('fastest')
    all_turtles.append(new_turtle)


# Inheritence Example
class Food(Turtle):
    # no need to create a new_turtle from Turtle()
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)


# file handling
# In day 24

# pandas library
import pandas

# whole spreadsheet = dataframe
data = pandas.read_csv("weather_data.csv")
print(data)  # Data table
# column = series in pandas
print(data["condition"])  # Column
print(data.condition)
# dataframe to dictionary
data_dict = data.to_dict()
# series to list
data_list = data["temp"].to_list()
# Print a row
print(data[data.day == "Monday"])
print(data[data["temp"] == data["temp"].max()])

# Comparing for a specific column value
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

# Get actual value from a column of a row
print(desired_row.state.item())

# List comprehension

# new_array = [new_item for item in array]
# upper_case_names = [name.upper() for name in names if len(name) > 4]
# list, tuples,range, string all are python sequences .i.e. they have a order

# Dictionary Comprehension
# new_dict = {item for item in iterable}
# dictionary = {key: value for (key, value) in iterable}

# items() returns a tuple
# new_dict = {key:value for (key,value) in old_dict.items() if test}

# *args 
# PASS unlimited parameters to function and loop over them also access them by args[0]
# args is a tuple
# **kwargs
# def calculate(n,**kwargs):
#     n+=kwargs['add']  #3
#     n*=kwargs['multiply']  #9
#     n-=kwargs['subtract'] #4
#     n/=kwargs['divide'] #1
#     print(n)
# calculate(1,add=2,multiply=3,divide=4,subtract=5)


# Email code smtplib


# import smtplib
# import random
#
# with open("quotes.txt") as quotes:
#     quotes_list = quotes.readlines()
#
# my_email = ""
# password = ""
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# random_quote = random.choice(quotes_list)
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,to_addrs="",
#                     msg=f"Subject:Testing Email\n\n{random_quote}")
# connection.quit()


# APIs
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
# for handling error
response.raise_for_status()
