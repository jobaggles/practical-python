# pcost.py
#
# Exercise 1.27
import csv


def portfolio_cost(filename):
    portfolio_total = 0
    filepath = "Data/" + filename
    with open(filepath, "rt") as f:
        next(f)
        for line in csv.reader(f):
            try:
                float(line[1])
            except ValueError:
                print(
                    f"Could not convert stock {line[0]}, perhaps it has missing values."
                )
                continue
            portfolio_total = portfolio_total + (float(line[1]) * float(line[2]))
    print(portfolio_total)
