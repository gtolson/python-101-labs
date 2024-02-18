# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


string_1 = input("enter string 1: ")
string_2 = input("enter string 2: ")
string_3 = input("enter string 3: ")

if len(string_1) > len(string_2) and len(string_1) > len(string_3):
    print(f"{len(string_1)}, {string_1})")
elif len(string_2) > len(string_1) and len(string_2) > len(string_3):
    print(f"{len(string_2)}, {string_2})")
else: 
    print(f"{len(string_3)}, {string_3})")  