print("hello world"[0])
# underscores are ignored
mystery = 734_529.678
print(mystery)

score = 0
heigth= 2.15
isWinning = True

# F string
print(f"Your score is {score}")


# random numbers
# produces a number including 0 and 100
import random
# generates random interger
random.randint(0,100)
# Returns the next random floating point number between [0.0 to 1.0)
random.random()  
# Random
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
print(random.choice(a))
#Inbuilt python functions
sum(a)
len(a)
max(a)
min(a)
# append and add in lists
fruits = []

fruits+="orange"

print(fruits)
#['o', 'r', 'a', 'n', 'g', 'e']

#Importing module 
import python_file_name
# or
from other_python_pile import word_list,logo,stages

# Keyword Argument
def greet_with_name(name, location):
  print(f"Hello {name}")
  print(f"Your location is {location}")

greet_with_name(location="Delhi",name="Sujal")
 

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

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

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

travel_log[0] = "Sujal"  #Valid
print(travel_log[0]) #can produce error if key not found i.e. if 0 is not any key

# Scope
gamelevel = 3
enemies = ["skeleton","zombie","alien"]

if gamelevel < 5:
  new_enemy  = enemies[0]

print(new_enemy)  #valid
# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.
#scope with function
gamelevel = 3
enemies = ["skeleton","zombie","alien"]
# function creates a local scope.
def fun():

  if gamelevel < 5:
    new_enemy  = enemies[0]
  # print(new_enemy)  #Valid
fun()
print(new_enemy)  #Invalid

# Using global variables can lead to bugs
#they should be used only for making global constants


# This is valid code even if we dont pass enemies as argument
enemies =1

def inc_enemy():
    print(f"enemy is {enemies} ")
    return enemies+100

print(inc_enemy())

# the point being we cannot modify global variable inside a function
