# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv


def parse_csv(filename, cols=None):
    '''
    Parse a CSV file into a list of records
    '''
    if cols is None:
        cols = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        if cols:
            headers = cols

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
