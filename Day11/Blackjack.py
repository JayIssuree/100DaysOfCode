import random
from Art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 8, 9, 10, 10, 10, 10]
playing = True

def printPlayerScore(array):
    arrStr = str(array)
    scoreStr = str(sum(array))
    message = "Your cards: " + arrStr + ", current score: " + scoreStr
    print(message)

def printComputerCard(array):
    firstCard = str(array[0])
    message = "Computer's first card: " + firstCard
    print(message)

def printComputerScore(array):
    arrStr = str(array)
    scoreStr = str(sum(array))
    message = "Computer's cards: " + arrStr + ", current score: " + scoreStr
    print(message)

def winMessage(player, computer):
    playerScore = sum(player)
    computerScore = sum(computer)
    if playerScore > 21 and computerScore > 21:
        message = "You both lose!"
    elif computerScore > 21:
        message = "Computer went over. You win!"
    elif playerScore > 21:
        message = "You went over. You lose!"
    elif playerScore > computerScore:
        message = "You win!"
    elif computerScore > playerScore:
        message = "You lose!"
    else:
        message = "It's a draw!"
    print(message)

def change11(score):
    total = sum(score)
    if total > 21 and 11 in score:
        score[score.index(11)] = 1
    return score

def newGame():
    userFinished = False
    player = []
    computer = []

    for _ in range(2):
        player.append(random.choice(cards))
        computer.append(random.choice(cards))
    
    while not userFinished:
        printPlayerScore(player)
        printComputerCard(computer)
        if sum(player) > 21:
            userFinished = True
        else:
            hit = raw_input("Type 'y' to get another card, type 'n' to pass: ")
            if hit is "y":
                player.append(random.choice(cards))
                player = change11(player)
            else:
                userFinished = True
    
    while sum(computer) < 17 or (sum(player) <= 21 and sum(computer) < sum(player)):
        computer.append(random.choice(cards))
        computer = change11(computer)
    
    printPlayerScore(player)
    printComputerScore(computer)
    winMessage(player, computer)


while(playing):
    startGame = raw_input("Do you want to start a new game of blackjack? Type 'y' or 'n': ")
    if startGame is "n":
        playing = False
    else:
        newGame()