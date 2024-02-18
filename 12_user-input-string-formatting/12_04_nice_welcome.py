# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


user_name = input("Please enter your name: ")

user_name_split = user_name.split()
first_name = user_name_split[0]

print(f"Welcome {first_name} glad to see you!")