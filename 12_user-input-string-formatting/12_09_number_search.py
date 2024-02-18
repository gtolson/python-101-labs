# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


user_number = int(input("Please enter a number between 1 an 1,000,000: "))

while True: 
    for user_number in range(1,1000000):
        print(f"Number {user_number} found")
        break
    break