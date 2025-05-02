import random
print("Welcome to rock paper scirssors game")

computer= random.randint(1,3)
player= int(input(" enter 1 for rock, 2 for paper and 3 for scissors "))

if computer==1 and player==1:
    print("it a draw")
elif computer==1 and player==2:
    print("you win")
elif computer==1 and player==3:
    print("you loss try again")
elif computer==2 and player==1:
    print("you loss try again")
elif computer==2 and player==2:
    print("it's a draw")
elif computer==2 and player==3:
    print("you win")
elif computer==3 and player==1:
    print("you win")
elif computer==3 and player==2:
    print("you loss try again")
elif computer==3 and player==3:
    print("it is a draw")
else:
    print("invalid input restart the game and enter a number from one to three")

