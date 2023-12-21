# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as pf:
        rows = csv.reader(pf)
        next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                cost = float(row[2].strip())
                total_cost = total_cost + (shares * cost)
            except ValueError:
                print(f'Problem parsing a value in the row {row}')

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

the_cost = portfolio_cost(filename)
print(f'Total cost {the_cost}')
