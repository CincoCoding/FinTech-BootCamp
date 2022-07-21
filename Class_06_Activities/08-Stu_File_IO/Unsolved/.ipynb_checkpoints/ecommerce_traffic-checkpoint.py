## -*- coding: utf-8 -*-
#"""Student Do: E-Commerce Traffic.
#
#This script will parse through a text file and sum the total
#number of customers and the count of days in the text file to
#calculate the daily average of customer traffic for an e-commerce
#business.
#"""
#
## @TODO: From the pathlib library, import the main class Path
#from pathlib import Path
#import csv
#
## @TODO: Check the current directory where the Python program is executing from
#print(f"Current Working Directory: {Path.cwd()}")
#
## @TODO: Set the path using Pathlib
#filepath = Path("C:/Users/range/Documents/FinTech BootCamp/Class_6_Activities/08-Stu_File_IO/Resources/customer_traffic.txt")
#
## Initialize variables
#customer_total = 0
#day_count = 0
#
## @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
#with open(filepath, "r") as file:
#    
#    # @TODO: Parse the file line by line
#    line_num = 1
#    for line in file:
#        
#        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
#        number = int(line)
#        customer_total += number
#        day_count += 1
#
#        # @TODO: Sum the total and count of the numbers in the text file
#print(f"customer total: {customer_total}")
#print(f"day count: {day_count}")
#print("-----------------------")
#
## @TODO: Print out customer_total and day_count
#daily_average = customer_total / day_count
#print(f"daily average: {daily_average}")
#
#
## @TODO: Calculate the average
#
#
#
## @TODO: Set output file name
#output_path = "output.txt"
#
## @TODO: Open the output path as a file object
#with open(output_path, "w") as file:
#    # @TODO: Write daily_average to the output file, convert to string
#    file.write(f"There were {customer_total} customers over the course of {day_count} days. \n")
#    file.write(f"The daily average was {daily_average}")

# -*- coding: utf-8 -*-
"""Student Do: E-Commerce Traffic.

This script will parse through a text file and sum the total
number of customers and the count of days in the text file to
calculate the daily average of customer traffic for an e-commerce
business.
"""

# @TODO: From the pathlib library, import the main class Path
from pathlib import Path

# @TODO: Check the current directory where the Python program is executing from
print(f"Current Working Directory: {Path.cwd()}")


# @TODO: Set the path using Pathlib
file = Path('C:/Users/range/Documents/FinTech BootCamp/Class_6_Activities/08-Stu_File_IO/Resources/customer_traffic.txt')

# Initialize variables
customer_total = 0
day_count = 0

# @TODO: Open the file in "read" mode ('r') and store the contents in the variable 'file'
with open(file, 'r') as file:
    
    # @TODO: Parse the file line by line
    for line in file:

        # @TODO: Convert the number in the text file from string to int (allows for numerical calculations)
        number = int(line)

        # @TODO: Sum the total and count of the numbers in the text file
        customer_total += number
        day_count += 1

# @TODO: Print out customer_total and day_count
print(f"customer_total: {customer_total}")
print(f"day_count: {day_count}")
print("-----------------------")



# @TODO: Calculate the average
daily_average = customer_total / day_count
print(f'daily_average: {daily_average}')


# @TODO: Set output file name
output_path = 'output1.txt'

# @TODO: Open the output path as a file object
with open(output_path, 'w') as file:
      
    # @TODO: Write daily_average to the output file, convert to string
      file.write(f'There were {customer_total} customers over the course of {day_count} days.\n')
      file.write(f'The average daily customer traffic is {daily_average} per day.')