# Programmers: Grace Armstrong & James Broderick
# Course: CS151, Prof. Mehri
# Date: 10.3.21
# Lab Number: 3
# Program Inputs: weight, distance
# Program Outputs: cost

# Do not accept values of 0 or less for the weight of the package.
# Do not accept weights of more than 20 kg (this is the maximum weight the company will ship).
# Do not accept distances of less than 10 miles or more than 3,000 miles.
# These are the minimum and maximum shipping distances of the company.

import math

weight = float(input("Enter weight of the item to ship: "))
distance = float(input("Enter distance of travel in miles: "))

if weight > 0 and weight <= 2 and distance >= 10 and distance <= 3000:
    rate = 1.1
    total_cost = math.ceil(rate * distance / 500)
    print(total_cost)
elif weight > 2 and weight <= 6 and distance >= 10 and distance <= 3000:
    rate = 2.2
    total_cost = math.ceil(rate * distance / 500)
    print(total_cost)
elif weight > 6 and weight <= 10 and distance >= 10 and distance <= 3000:
    rate = 3.7
    total_cost = math.ceil(rate * distance / 500)
    print(total_cost)
elif weight > 10 and weight <= 20 and distance >= 10 and distance <= 3000:
    rate = 4.8
    total_cost = math.ceil(rate * distance / 500)
    print(total_cost)