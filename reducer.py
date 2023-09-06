#!/usr/bin/env python
import sys

# Initialize variables to store aggregated data
total_oldbalanceorg = 0
total_newbalanceorig = 0
total_amount = 0
total_oldbalancedest = 0
total_newbalancedest = 0
total_count = 0

# Read input from stdin
for line in sys.stdin:
    # Parse the line into values
    values = line.strip().split('\t')

    # Extract the values from the line
    oldbalanceOrg = float(values[0])
    newbalanceOrig = float(values[1])
    amount = float(values[2])
    oldbalanceDest = float(values[3])
    newbalanceDest = float(values[4])
    count = int(values[5])

    # Accumulate the values
    total_oldbalanceorg += oldbalanceOrg
    total_newbalanceorig += newbalanceOrig
    total_amount += amount
    total_oldbalancedest += oldbalanceDest
    total_newbalancedest += newbalanceDest
    total_count += count

# Perform further processing or aggregation as needed
# For example, you can calculate averages, totals, or percentages

# Emit the final result as output
print(f'Total Old Balance Org: {total_oldbalanceorg}')
print(f'Total New Balance Orig: {total_newbalanceorig}')
print(f'Total Amount: {total_amount}')
print(f'Total Old Balance Dest: {total_oldbalancedest}')
print(f'Total New Balance Dest: {total_newbalancedest}')
print(f'Total Count: {total_count}')

