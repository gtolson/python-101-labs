# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment_amount = int(input("Enter the amount you would like to invest: "))
interest_rate = int(input("Enter the interest rate: "))
duration = int(input("Enter number of years to invest: "))

interest_rate_calc = interest_rate/100

result = (investment_amount * interest_rate_calc + investment_amount) * duration

print(f"After a duration of {duration} years the total value will be: {result}")