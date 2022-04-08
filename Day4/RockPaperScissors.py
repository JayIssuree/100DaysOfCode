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

asci = [rock, paper, scissors]
player_choice = int(raw_input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice = random.randint(0, 2)

print("You chose:")
print(asci[player_choice])

print("Computer chose:")
print(asci[int(computer_choice)])

if player_choice == 0:
    if computer_choice == 0:
        print("Draw!")
    if computer_choice == 1:
        print("You lose!")
    if computer_choice == 2:
        print("You win!")

if player_choice == 1:
    if computer_choice == 0:
        print("You win!")
    if computer_choice == 1:
        print("Draw!")
    if computer_choice == 2:
        print("You lose!")

if player_choice == 2:
    if computer_choice == 0:
        print("You lose!")
    if computer_choice == 1:
        print("You win!")
    if computer_choice == 2:
        print("Draw!")