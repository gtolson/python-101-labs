# Using a loop, sum all numbers from the `start` to the `stop` number.
# The sequence should consist only of integers from 1 to 100.
# The output of your calculation should look like this:
#
#      The sum is: 5050

start = 1
stop = 101
sum_num = 0

for num in range(start,stop):
    sum_num += num
print(f"The sum is: {sum_num}")   
    