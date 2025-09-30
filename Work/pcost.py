# pcost.py
#
# Exercise 1.27
from pprint import pprint
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


def read_portfolio(filename):
    list = []
    portfolio_total = 0
    with open(filename, "rt") as f:
        next(f)
        for line in csv.reader(f):
            try:
                t = (line[0], int(line[1]), float(line[2]))
                list.append(t)
                portfolio_total += int(line[1]) * float(line[2])
            except ValueError:
                print(
                    f"Could not convert stock {line[0]}, perhaps it has missing values."
                )
                continue
    return list, portfolio_total


def read_portfolio_dict(filename):
    list = []
    portfolio_total = 0
    with open(filename, "rt") as f:
        next(f)
        for line in csv.reader(f):
            try:
                t = {"name": line[0], "shares": int(line[1]), "price": float(line[2])}
                list.append(t)
                portfolio_total += t["shares"] * t["price"]
            except ValueError:
                print(
                    f"Could not convert stock {line[0]}, perhaps it has missing values."
                )
                continue
    return list, portfolio_total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Passing default file path Data/portfolio.csv")
    filename = "Data/portfolio.csv"

# cost = portfolio_cost(filename)
# print("Total cost:", cost)

portfoli0, total = read_portfolio_dict(filename)
pprint(portfoli0)  # this can be used to print a large dictionary nicely.
# print(portfoli0)
