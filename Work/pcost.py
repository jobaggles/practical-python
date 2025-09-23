# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    portfolio_total = 0
    with open(filename, "rt") as f:
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
    return portfolio_total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Passing default file path Data/portfolio.csv")
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
