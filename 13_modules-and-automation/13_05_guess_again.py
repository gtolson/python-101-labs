# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
#!/usr/bin/python

from random import randint


num = randint(1, 10)
guess = 0
count = 0

while guess != num:
    guess = input("please guess a number 1 - 10: ")
    if guess.isalpha():
        print("You have not entered a number between 1 and 10, please try again...")
        continue
    guess = int(guess)
    if guess >= 10:
        print("You have not entered a number between 1 and 10, please try again...")
        continue
    count += 1
    if count >= 10:
        print("You have run out of attempts please try again!")
        exit()
    
print(f"Congrats {guess} is the correct number, it only took you {count} attempts to figure it out!")