# What data type is the variable `mystery` at the end of the script?
# What data types does it hold at certain points earlier in the script?

mystery = None
# no value
print(type(mystery))
mystery = False
print(type(mystery))
mystery = "Sommerfeld"
# string
print(type(mystery))
mystery = 137
#int
print(type(mystery))
mystery = mystery + 0.0
# float
print(type(mystery))
mystery = [1, 2, 3]
print(type(mystery))
mystery = {"color": "green", "number": 1}
print(type(mystery))
