# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user_input = input("What about food do you like? ")
user_input_len = len(user_input)
user_input_sar = ""

for index in range(len(user_input)):
    if index % 2:
        user_input_sar += user_input[index].upper()
    else: 
        user_input_sar += user_input[index].lower()
        
print(f"{user_input_sar}")