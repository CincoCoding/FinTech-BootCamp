# -*- coding: utf-8 -*-
"""
Zero-Coupon Bond Valuation.

This script will calculate the present value of zero-coupon bonds, compare the present value to the price of the bond, and determine the corresponding action (buy, not buy, neutral).
"""

# @TODO: Create a function to calculate present value
def present_value(price, future_value, discount_rate, compounding_periods, years):
    # PV =  FV / (1 + r/n) t*n 
    PV = future_value / ((1+(discount_rate/compounding_periods)) ** (compounding_periods * years))
    #buy/sell/neutral?
    if PV > price:
        return "Buy"
    elif PV < price:
        return "Don't Buy"
    else:
        return "Neutral"

# Intialize the zero-coupon bond parameters, assume compounding period is equal to 1
price = 700
future_value = 1000
discount_rate = .1
compounding_periods = 1
years = 5

# @TODO: Call the calculate_present_value() function and assign to a variables
# print it out
reccomendation = present_value(price, future_value, discount_rate, compounding_periods, years)
print(reccomendation)
# @TODO: Determine if the bond is worth it
#NO