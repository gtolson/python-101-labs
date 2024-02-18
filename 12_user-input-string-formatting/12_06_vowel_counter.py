# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


user_string = input("Please enter a string of text: ")
vowels = ["a","e","i","o","u"]
vowel_counter = 0

for char in user_string:
    char == char.lower()
    for vowel in vowels:
        if char == vowel:
            vowel_counter += 1
            
print(f"There are {vowel_counter} vowels in the string:")