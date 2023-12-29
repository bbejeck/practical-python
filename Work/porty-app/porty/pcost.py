# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as pf:
        rows = csv.reader(pf)
        headers = next(rows)
        for n, row in enumerate(rows, start=1):
            try:
                d = dict(zip(headers, row))
                shares = int(d['shares'])
                cost = float(d['price'].strip())
                total_cost = total_cost + (shares * cost)
            except ValueError:
                print(f'Row {n}: Couldn\'t parse row {row}')

    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

the_cost = portfolio_cost(filename)
print(f'Total cost {the_cost}')
