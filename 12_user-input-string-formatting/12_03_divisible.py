# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

user_number = int(input("Please enter a number between 1 an 1,000,000: "))

result = user_number % 3

if result == 0:
    print(f"{user_number} is divisible by 3")
else:
    print(f"{user_number} is NOT divisible by 3")