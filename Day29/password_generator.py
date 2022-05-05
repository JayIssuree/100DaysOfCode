#Password Generator Project
import random

class Password_Generator:

  def __init__(self):
    self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    self.NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    self.NR_LETTERS = random.randint(8, 10)
    self.NR_SYMBOLS = random.randint(2, 4)
    self.NR_NUMBERS = random.randint(2, 4)

  def generate(self):
    password_list = [random.choice(self.LETTERS) for _ in range(self.NR_LETTERS)] + [random.choice(self.SYMBOLS) for _ in range(self.NR_SYMBOLS)] + [random.choice(self.NUMBERS) for _ in range(self.NR_NUMBERS)]
    random.shuffle(password_list)
    password = "".join(password_list)

    return password