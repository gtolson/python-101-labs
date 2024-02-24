# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it


#!/usr/bin/python

hgm_word = "person"
hgm_letters = "______"

game_statement = "Welcome to the hangman game, you will have 20 attempts to guess the letters that make up the winning word. Good Luck!"

print(game_statement)

count = 20

while count != 0 and hgm_letters!= hgm_word:
    print(f"You have {count} remaining attempts")
    print(hgm_letters)
    user_guess = input("Please enter a letter you believe is in the word: ")
    user_guess = user_guess.lower()
    count -= 1
    if user_guess not in hgm_word:
        print("This letter is not in the winning word")
        print("")
        continue
        print(hgm_letters)
    elif user_guess in hgm_word:
        user_guess_index = hgm_word.find(user_guess)
        user_guess_index_plusone = user_guess_index + 1
        hgm_letters = hgm_letters[:user_guess_index] + user_guess + hgm_letters[user_guess_index + 1:]
        print(hgm_letters)
        continue    

    
if count == 0:
    print("Sorry you are out of attmepts, please try again!")
    
print(f"Congrats you found all the letters to the winning word: {hgm_letters}")