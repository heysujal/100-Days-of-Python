# using functions https://replit.com/@heysujal/guess-the-number-final-1#main.py

import random

print("Welcome to number guessing game")

difficulty = input("Select difficulty easy or hard\n")

if difficulty=="easy":
    lives = 10
else:
    lives = 5 


answer = random.randint(1,100)

# print(lives)       
while lives > 0:
    guess = int(input("Enter a number to guess"))

    if guess == answer:
        print(f"You got it.Answer was {answer}")
        lives = 0
    else:
        lives-=1
        if guess < answer:
            print("Too low")
        else :
            print("Too high")

        print("Guess Again.")        
        if lives==0:
            print(f"You ran out of guesses.The answer was {answer}.\n You lose 😭")
        else:
            print(f"You have {lives} guesses left.\n") 