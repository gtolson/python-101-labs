# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


user_string = input("Please enter a string of text to search: ")
symbol_string = input("Please enter a symbol of your choice: ")

first_letter = user_string[0]
new_string = user_string.replace(first_letter, symbol_string)

#for char in user_string:
#    if char == first_letter:
#        char.replace(char, symbol_string)
#        new_string.append(char)
#    new_string.append(char)
    
print(f"Result string: {new_string}")