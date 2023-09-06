#!/usr/bin/env python
import sys
import pandas as pd

# Read input from stdin
for line in sys.stdin:
    # Parse the line into a list of values
    values = line.strip().split(',')

    # Extract the relevant columns
    oldbalanceOrg = float(values[0])
    newbalanceOrig = float(values[1])
    amount = float(values[2])
    oldbalanceDest = float(values[3])
    newbalanceDest = float(values[4])

    # Process the values as needed
    # For example, you can perform calculations, filter data, or create key-value pairs

    # Emit key-value pairs as output
    print(f'{oldbalanceOrg}\t{newbalanceOrig}\t{amount}\t{oldbalanceDest}\t{newbalanceDest}\t1') # Use tab as the separator and add a count of 1 as the value

