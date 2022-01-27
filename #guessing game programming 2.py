#guessing game programming 2 
import random
number = random.randint(1, 101)

tries = 0

#welcome message
print("\tWelcome to 'guess my number!'\t")
trigger = str(input("type start to start "))
while trigger == "start":
    guess = int(input("im thinking of a number 1-100... "))

    while guess != number:
        if guess > number:
            print("too high...")
            guess = int(input("Guess again... "))
            tries += 1
        elif guess < number:
            print("too low...")
            guess = int(input("Guess again... "))
            tries += 1

    while guess == number:
        print("You guessed it!!! yay!!")
        print("it only took you ", tries, "tries!")
        break
    trigger = str(input("Type start to go again and end to end. "))


print("Thanks for playing!")