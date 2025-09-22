# pcost.py
#
# Exercise 1.27
portfolio_total = 0
updated_contents = list
with open("Data/portfolio.csv", "rt") as f:
    next(f)  # skip headers
    for line in f:
        line = line.split(",")
        portfolio_total = portfolio_total + (float(line[1]) * float(line[2]))
    print(portfolio_total)
