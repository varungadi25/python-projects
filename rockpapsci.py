import random
print("Welcome to Rock, Paper, Scissors!")

rock = '''
    ______
---'  ____)
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
game_symbols = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_symbols[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose:" )
print(game_symbols[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. you lost.")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")

elif user_choice == 1 and computer_choice == 0:
    print("You win!")

elif user_choice == 2 and computer_choice == 1:
    print("You win!")

elif user_choice == computer_choice:
    print("It's a draw!")

else:
    print("You lose!")

