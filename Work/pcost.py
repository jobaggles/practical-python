# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    portfolio_total = 0
    filepath = "Data/" + filename
    with open(filepath, "rt") as f:
        next(f)
        for line_number, line in enumerate(f, 1):
            line = line.split(",")
            try:
                float(line[1])
            except ValueError:
                print(
                    f"Could not convert line {line_number}, perhaps it has missing values."
                )
                continue
            portfolio_total = portfolio_total + (float(line[1]) * float(line[2]))
    print(portfolio_total)
