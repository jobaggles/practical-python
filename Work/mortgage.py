# mortgage.py
#
# Exercise 1.7
# mortgage.py
start_month = int(input("Start Month: "))
end_month = int(input("End Month: "))
bonus_payment = int(input("Extra Payment: "))

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while principal > 0:
    if principal < payment:
        payment = principal * (1 + rate / 12)
    if end_month >= month >= start_month:
        principal = principal * (1 + rate / 12) - (payment + bonus_payment)
        total_paid = total_paid + payment + bonus_payment
        print(month, " ", total_paid, " ", principal)
    else:
        principal = principal * (1 + rate / 12) - (payment)
        total_paid = total_paid + payment
        print(month, " ", total_paid, " ", principal)
    month += 1
print("Total paid", total_paid)
print("Months:", month)
