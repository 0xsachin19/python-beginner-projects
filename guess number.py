import random
print("guessing game")
computer_guess=random.randint(1,100)
print("you have 3 choice")
chance=3
while chance>0:
    user_guess=int(input("enter your number: "))
    if computer_guess>user_guess:
        print("you guessed low")
        chance=chance-1
    elif computer_guess<user_guess:
        print("you guessed high")
        chance=chance-1
    else:
        print("you guessed correctly")
        break
if chance==0:
    print("you lost! number was: {computer_guess}")
    
