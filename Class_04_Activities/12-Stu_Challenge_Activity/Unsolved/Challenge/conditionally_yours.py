"""
Conditionally Yours

Pseudocode:


"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
original_price = 4.23

# Create integer variable for current_price
current_price = 5.80

# Create float for threshold_to_buy
threshold_to_buy = 2.00

# Create float for threshold_to_sell
threshold_to_sell = -2.00

# Create float for portfolio balance
portfolio_balance = 580.00

# Create float for balance check
balance_check = 400.00

# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase * 100) / original_price

# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(current_price)

# Print percent increase
print(percent_increase)

# Determine if stock should be bought or sold
if percent_increase > threshold_to_buy:

# Print recommendation
    print("Recommendation: " + recommendation)
    print()
    print("But wait a minute... lets check your excess equity first.")


# Challenge

# Declare balance variable as a float
balance = 20.00

# Declare balance_check variable
balance_check = balance * 5

# Compare balance to recommendation, checking whether or not balance is 5 times more than current_price
print(f"You currently have ${balance} in excess equity available in your portfolio.")

