name = input("Enter your name: ")
print(f"Welcome to the game {name}, Lets Begin!")

answer = input("You have come to a dirt road it ends here. It goes left and right which way will you go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and eaten by an alligator, you lost the game!!!")
    elif answer == "walk":
        print("You walk for miles and ran out of water, you lost the game!!!")
    else:
        print("Not a valid option! You Lose!!!")
elif answer == "right":
    answer = input("You come across an old bridge it can fall anytime do you want to cross it or go back? cross to cross the bridge and back to go back: ").lower()
    
    if answer == "back":
        print("You go back and lose the game!!!")
    elif answer == "cross":
        answer = input("You cross the bridge meet a stranger. Do you want to talk to him? (Yes/No): ").lower()

        if answer == "yes":
            print("You talked to the stranger and they helped you out of the game!")
            print("************************************")
            print("Congratulations! You Won the Game!!!")
            print("************************************")
        elif answer == "no":
            print("You ignored the stranger and got lost! You Lose!!!")
        else:
            print("Not a valid option! You Lose!!!")
    else:
        print("Not a valid option! You Lose!!!")
else:
    print("Not a valid option! You Lose!!!")

