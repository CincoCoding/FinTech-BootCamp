# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)
banks = { "JP Morgan Chase": 327,
 "Bank of America": 302,
 "Citigroup": 173,
 "Wells Fargo": 273,
 "Goldman Sachs": 87,
 "Morgan Stanley": 72,
 "U.S. Bancorp": 83,
 "TD Bank": 108,
 "PNC Financial Services": 67,
 "Capital One": 47,
 "FNB Corporation": 4,
 "First Hawaiian Bank": 3,
 "Ally Financial": 12,
 "Wachovia": 145,
 "Republic Bancorp": .97,

}


# @TODO: Change the market cap for 'Citigroup'
banks['Citigroup'] = 170
print(banks)


# @TODO: Add a new bank and market cap pair
banks['American Express'] = 33
print(banks)


# @TODO: Remove a bank from the dictionary
del banks['Wachovia']
print(banks)


# Mega Cap: Firms with a market capitalization over $300 billion.
# Large Cap: Firms with a market capitalization over 10 billion. ...
# Mid Cap: A market capitalization between $2 and $10 billion.
# Small Cap: A market capitalization between $300 million and $2 billion.

    # @TODO: Calculate sum of market caps and number of banks in the dictionary
count = 0
total_market_cap = 0
for i in banks:
    total_market_cap += banks[i]
    count += 1
print(total_market_cap, count)


    # @TODO: Logic to determine min value and associated key
minimum = float('inf')
for i in banks:
    if banks[i] < minimum:
        minimum = banks[i]
print(minimum)


    # @TODO: Logic to determine max value and associated key
maximum = float('-inf')
for i in banks:
    if banks[i] > maximum:
        maximum = banks[i]
print(maximum)


    # @TODO: Group banks by categories of market caps
MEGA_CAP = []
for i in banks:
    if banks[i] > 300:
        MEGA_CAP.append(i)
print(MEGA_CAP)
        
LARGE_CAP = []
for i in banks:
    if banks[i] <= 300 and banks[i] > 10:
        LARGE_CAP.append(i)
print(LARGE_CAP)

MID_CAP = []
for i in banks:
    if banks[i] <= 10 and banks[i] > 2:
        MID_CAP.append(i)
print(MID_CAP)

SMALL_CAP = []
for i in banks:
    if banks[i] <= 2 and banks[i] > 0.300:
        SMALL_CAP.append(i)
print(SMALL_CAP)


# @TODO: Calculate average market cap of banks in the dictionary
average_market_cap = 0
for i in banks:
    average_market_cap += banks[i]
average_market_cap = average_market_cap/count
print("{:.2f}".format(average_market_cap))

