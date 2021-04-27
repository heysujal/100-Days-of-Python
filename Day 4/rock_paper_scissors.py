import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbol_list = [rock,paper,scissors]
user_choice = int(input("Welcome to rock, paper and scissors\n0 for rock, 1 for paper, and 2 for scissors"))
print("Your choice\n" + symbol_list[user_choice])
#computer_choice = random.randint(0,2)
computer_choice = symbol_list.index(random.choice(symbol_list))
print("Computer choice\n"+ symbol_list[computer_choice])

if user_choice>=3 or user_choice < 0:
  print("You entered an invalid number!")
else:   
  if (computer_choice == 0 and user_choice ==1 ) or (computer_choice==2 and user_choice==0) or (computer_choice==1 and user_choice==2):
    print("You win!")
  elif computer_choice==user_choice:
    print("Draw!")
  else:
    print("You lose!")

 