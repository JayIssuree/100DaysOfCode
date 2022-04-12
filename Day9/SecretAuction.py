# -*- coding: utf-8 -*-
import os

print("Welcome to the secret auction")

bidding_complete = False
dictionary = {}

while(not bidding_complete):
    name = raw_input("What is your name?: ")
    bid = int(raw_input("What is your bid? £"))
    dictionary[name] = bid
    additional_bidders = raw_input("Are there any other bidders? Type 'yes' or 'no'.")
    if(additional_bidders == "no"):
        bidding_complete = True
    os.system('clear')

winner_name = max(dictionary, key=dictionary.get)
winner_bid = str(dictionary[winner_name])
message = "The winner is " + winner_name + " with a bid of £" + winner_bid
print(message)