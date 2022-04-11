import random
from Words import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
answer = []
for letter in chosen_word:
    answer.append("_")
lives = 6
end_of_game = False

print(answer)

while not end_of_game:
    guess = raw_input("Guess a letter: ").lower()
    index = 0
    if guess in chosen_word:
        for letter in chosen_word:
            if guess == letter:
                answer[index] = guess
            index += 1
        print("You guessed " + guess + ", that is in the word!")
    else:
        print("You guessed " + guess + ", that is not the word!")
        lives -= 1
    print(stages[lives])
    index = 0
    if lives <= 0:
        end_of_game = True
        print("You Lose! The word was: " + chosen_word)
    if "_" not in answer:
        end_of_game = True
        print("You Win!")
    print(answer)
