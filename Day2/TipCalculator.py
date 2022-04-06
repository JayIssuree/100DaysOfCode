# -*- coding: utf-8 -*-
print("Welcome to the tip calculator")
totalBill = float(raw_input("What was the total bill? £"))
tipPercent = float(raw_input("What percentage would you like to give? "))
numberOfPeople = int(raw_input("How many people want to split the bill? "))

pricePerPerson = totalBill * (1 + tipPercent/100) / numberOfPeople
message = "Each person should pay: £" + str(round(pricePerPerson, 2))
print(message)