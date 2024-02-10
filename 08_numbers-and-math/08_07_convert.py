# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

#decimal is lost when doing float to int

number1 = 5
print(number1)
print(type(number1))
number1 = float(number1)
print(number1)
print(type(number1))

number2 = 10.0
print(number2)
print(type(number2))
number2 = int(number2)
print(number2)
print(type(number2))


div = number2 / number1
print(div)

mul = number2 * number1
print(mul)