import random
import os
from GameData import data

def retreiveData():
    return random.choice(data)

def printInformationString(account):
    return account["name"] + ", " + account["description"] + " from " + account["country"] + "."

def printComparison(accountA, accountB):
    print("Compare A: " + printInformationString(accountA))
    print("VS.")
    print("Against B: " + printInformationString(accountB))

def game():
    game_over = False
    score = 0
    b = retreiveData()

    while not game_over:
        os.system('clear')

        if score > 0:
            print("You're right! Current score: " + str(score))

        a = b
        b = retreiveData()

        while a == b:
            b = retreiveData()

        printComparison(a, b)

        answer = raw_input("Who has more followers? Type 'A' or 'B': ")
        if (answer is "B" and b["follower_count"] < a["follower_count"]) or (answer is "A" and a["follower_count"] < b["follower_count"]):
            print("Sorry, that's wrong. Final score: " + str(score))
            game_over = True
        elif (answer is not "A" and answer is not "B"):
            print("Incorrect input")
            game_over = True
        else:
            score += 1

game()