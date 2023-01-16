import random

number=random.randint(1,10)
guess=0
count=0

while guess!=number and guess!=exit:
    guess=input("You have to guess the number between 1 to 10: ")
    
    
    guess=int(guess)
    count+=1
    if guess not in range(1,10):
        print("You have to guess a number between 1 to 10")
    
    if guess==number:
        print("you guessed it right")

    elif guess<number:
        print("You guessed it too low")

    else:
        print("You guessed it too high") 
