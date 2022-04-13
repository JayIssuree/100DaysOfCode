from random import randrange

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

NUMBER = randrange(100)

difficulty = raw_input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    number_of_guesses = 10
else:
    number_of_guesses = 5

while number_of_guesses > 0:
    print("You have " + str(number_of_guesses) + " attmpts remaining to guess the number.")
    guess = int(raw_input("Make a guess: "))
    if guess > NUMBER:
        print("Too high")
    elif guess < NUMBER:
        print("Too low")
    else:
        print("Congratulations, you guessed correctly")
        break
    number_of_guesses -= 1
    if number_of_guesses > 0:
        print("Guess again")
    else:
        print("You took too many guesses")

print("The number I was thinking of was: " + str(NUMBER))