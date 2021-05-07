from art import logo,vs
from game_data import data
import random
import os

 
def get_random():
    return random.choice(data)


clear = lambda: os.system('cls')
is_game_over = False
option1 = get_random()
option2 = get_random()
score = 0

while not is_game_over:
    clear()
    # print("Higher Lower\n")
    print(logo)

    if score:
        print(f"You are right.Your current score is {score}")

    print(f"Compare A: {option1['name']},{option1['description']}, from {option1['country']}")

    # print("\nVS\n")
    print(vs)

    print(f"Against B: {option2['name']},{option2['description']}, from {option2['country']} ")

    if option1['follower_count'] > option2['follower_count']:
        answer = 'a'
    else:
        answer = 'b'

    # testing code
    # print("correct answer is ",answer)

    choice = input("Who has more instagram followers? Type 'A' or 'B': ").lower()
    if choice == answer:
        score+=1
        option1 = option2
        option2 = get_random()
    else:
        is_game_over = True
        print(f"You lose.Your final score is {score}")    