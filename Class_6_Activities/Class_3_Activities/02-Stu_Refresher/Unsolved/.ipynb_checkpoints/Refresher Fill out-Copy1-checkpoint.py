# -*- coding: utf-8 -*-
"""Refresher activity.

This script will use variables, conditionals, lists, dicts, and functions
to print out different greetings for customers based on their
business tier (determined by revenue).
"""

# List of dicts
customers = [
    { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
    { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
    { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
    { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
]

# @TODO Define a function that accepts a customer first_name, last_name, and
# revenue and returns a custom greeting with the full name.
# Use these ranges to determine the business tier (and corresponding message)
# for each customer.
#   Platinum = 3001+
#   Gold = 2001-3000
#   Silver = 1001-2000
#   Bronze = 0-1000
def create_greeting(first_name, last_name, revenue):
    # @TODO: YOUR CODE HERE!
    if revenue <= 1000:
        print(f'Hello Bronze Tier Member {first_name} {last_name}')
    elif revenue <= 2000:
        print(f'Hello Silver Tier Member: {first_name} {last_name}')
    elif revenue <= 3000:
        print(f'Hello Gold Tier Member: {first_name} {last_name}')
    else:
        print(f'Hello Platinum Tier Member: {first_name} {last_name}') 
        

# @TODO: Loop through the list of customers and use your function to print
# custom greetings for each customer.
for customer in customers:
    create_greeting(customer["first_name"], customer["last_name"], customer["revenue"])
        