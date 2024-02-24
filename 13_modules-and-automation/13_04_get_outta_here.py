# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

#!/usr/bin/python

import sys

while True:
    question = input("Please type in a word, if you want to exit type quit.")
    question = question.lower()
    if question == "quit":
        sys.exit()
    else:
        print(f"You entered {question}")
    