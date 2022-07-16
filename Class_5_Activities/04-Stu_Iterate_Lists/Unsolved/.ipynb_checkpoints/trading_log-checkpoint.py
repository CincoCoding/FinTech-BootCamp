# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables
total = 0
count = 0
minimum = float('inf')
maximum = float('-inf')
average = 0.00
profitable_days_count = 0
unprofitable_days_count = 0
profitable_days_percentage = 0
unprofitable_days_percentage = 0


# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses
profitable_days = []
unprofitable_days = []


# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]


# @TODO: Iterate over each element of the list
for pnl in trading_pnl:

    
    # @TODO: Cumulatively sum up the total and count
    total += pnl
print(total)


    # @TODO: Write logic to determine minimum and maximum values
for pnl in trading_pnl:
    if pnl < minimum:
        minimum = pnl
print(minimum)

for pnl in trading_pnl:
    if pnl > maximum:
        maximum = pnl
print(maximum)


    # @TODO: Write logic to determine profitable vs. unprofitable days
for pnl in trading_pnl:
    if pnl > 0:
        profitable_days.append(pnl)
    else:
        unprofitable_days.append(pnl)

print(profitable_days, unprofitable_days)


# @TODO: Calculate the average
for pnl in trading_pnl:
    average += pnl
average = average/len(trading_pnl)
print(average)


# @TODO: Calculate count metrics
profitable_days_count = len(profitable_days)
print(profitable_days_count)

unprofitable_days_count = len(unprofitable_days)
print(unprofitable_days_count)


# @TODO: Calculate percentage metrics
count = len(trading_pnl)
profitable_days_percentage = 100 * (profitable_days_count/count)
unprofitable_days_percentage = 100 * (unprofitable_days_count/count)
print(profitable_days_percentage, unprofitable_days_percentage)


