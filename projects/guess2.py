#!/usr/bin/python

import random

number = random.randint(1,10)
counter = 10

while counter != 0:
    print(f"you have {counter} tries to guess a number betweeh 1 and 10")
    guess = input("What is your guess?")
    guess = int(guess)
    counter -= 1
    if guess == number:
        print(f"Awesome! you guessed the number was {number}, you won. Thanks for playing !")
        exit()
    else:
        print(f"Your guess of {guess} was not correct")
        continue
print("You have run out of attempts to guess the correct number")