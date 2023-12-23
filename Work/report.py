# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
from math import floor


def read_portfolio(filename):
    portfolio = []
    with open(filename) as pf:
        rows = csv.reader(pf)
        headers = next(rows)
        for row in rows:
            d = dict(zip(headers, row))
            try:
                portfolio.append({"name": d['name'], "shares": int(d['shares']), "price": float(d['price'])})
            except ValueError:
                print(f'Problem parsing a value in the row {row}')

    return portfolio


def get_prices(filename):
    price_map = {}
    with open(filename) as price_file:
        rows = csv.reader(price_file)
        for row in rows:
            if row:
                price_map[row[0]] = row[1]

    return price_map


def print_row(row_info):
    print(f'{row_info[0]:>12} {row_info[1]:>12} {row_info[2]:>12} {row_info[3]:>12.2f}')


def make_report(portfolio, prices):
    dash = '-'
    portfolio_changes = []
    headers = ("Name", "Shares", "Price", "Change")
    for position in portfolio:
        if position['name'] in prices:
            delta = float(prices[position['name']]) - position['price']
            portfolio_changes.append((position['name'], position['shares'], prices[position['name']], delta))

    print(f'{headers[0]:>12} {headers[1]:>12} {headers[2]:>12} {headers[3]:>12}')
    print(f'{dash:-<12}  {dash:-<12} {dash:-<12} {dash:-<12}')
    for portfolio_change in portfolio_changes:
        print_row(portfolio_change)


portfolio = read_portfolio('Data/portfoliodate.csv')
prices = get_prices('Data/prices.csv')

# pprint(portfolio)
# pprint(prices)

make_report(portfolio, prices)
