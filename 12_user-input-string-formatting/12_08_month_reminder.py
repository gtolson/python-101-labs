# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    user_num = int(input("Enter in a number between 1 and 12: "))

    if user_num not in range(1,13):
        print("Please re-enter a number between 1 and 12: ")
        continue
    
    print(f"The month for the number you entered is: {months[user_num - 1]}")
    exit()
    