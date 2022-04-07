choice1 = raw_input("You are at a crossroads do you want to go \"left\" or \"right\"? ")

if choice1.upper() != "LEFT":
    print("Game Over!")
else:
    choice2 = raw_input("You are at a river, do you want to \"swim\" or \"wait\"? ")
    if choice2.upper() != "WAIT":
        print("Game Over!")
    else:
        choice3 = raw_input("You see 3 doors, which do you choose? \"red\", \"blue\" or \"yellow\"? ")
        if choice3.upper() != "YELLOW":
            print("Game Over!")
        else:
            print("You Win!")
