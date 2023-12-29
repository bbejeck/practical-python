# report.py
#
# Exercise 2.4
import csv
from . import fileparse
from .stock import Stock
from .portfolio import Portfolio


def read_portfolio(filename):
    portdicts = fileparse.parse_csv(filename,
                                    cols=['name', 'shares', 'price'])
    portfolio = [Stock(**d) for d in portdicts]
    
    return Portfolio(portfolio)


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


def make_report():
    portfolio = read_portfolio('Data/portfoliodate.csv')
    prices = get_prices('Data/prices.csv')
    dash = '-'
    portfolio_changes = []
    headers = ("Name", "Shares", "Price", "Change")
    for position in portfolio:
        if position['name'] in prices:
            delta = float(prices[position['name']]) - position['price']
            portfolio_changes.append((position['name'], position['shares'], prices[position['name']], delta))

    print_report(dash, headers, portfolio_changes)


def print_report(dash, headers, portfolio_changes):
    print(f'{headers[0]:>12} {headers[1]:>12} {headers[2]:>12} {headers[3]:>12}')
    print(f'{dash:-<12}  {dash:-<12} {dash:-<12} {dash:-<12}')
    for portfolio_change in portfolio_changes:
        print_row(portfolio_change)


if __name__ == '__main__':
    print(f'Running as main {__name__}')
    make_report()
else:
    print(f'It\'s being used as a library {__name__}')
