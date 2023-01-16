import random

number=random.randint(1,9)
guess=0
count=0

while guess!=number:
    guess=int(input("Guess a number between 1 to 9: "))
    count+=1
    if guess not in range(1,9):
        print("You have to guess a number between 1 to 9")
    
    if guess==number:
        print("you guessed it right")

    elif guess<number:
        print("You guessed it too low")

    else:
        print("You guessed it too high") 
