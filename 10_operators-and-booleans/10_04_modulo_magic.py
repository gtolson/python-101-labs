# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997
div = 7

for num in [num_1, num_2, num_3, num_4]:
    result = num % div
    if result == 0:
        print(f"{num} is divisible by {div}")
    else:
        print(f"{num} is NOT divisible by {div}")