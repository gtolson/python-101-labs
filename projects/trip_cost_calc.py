#!/usr/bin/python

miles_to_drive = float(input("How many mile do you intend to drive?: "))
mpg = float(input("How many miles per gallon does your car get?: "))
gas_per_gal = float(input("What is the cost of a gallon of Gas?: "))

total_cost = (miles_to_drive / mpg) * gas_per_gal

print(f"""The total cost of the trip:
Miles to drive: {miles_to_drive:>20}
Miles per gallon: {mpg:>18}
Gas cost per gallon: {gas_per_gal:>15}
Total Cost: {total_cost:>24}
""")