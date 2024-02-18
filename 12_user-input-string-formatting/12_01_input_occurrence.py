# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4


print("Welcome to the char index finder!")
user_string = input("Please enter a string of text to search: ")
letter_string = input("Please enter a letter in your string to find its index value: ")

letter_string_index = user_string.find(letter_string)

print(f"String input: {user_string}")
print(f"Letter input: {letter_string}")
print(f"Result: {letter_string_index}")
