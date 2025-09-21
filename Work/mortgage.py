# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
bonus_payment = 1000
bonus_duration = 12

while principal > 0:
    if bonus_duration > 0:
        principal = principal * (1 + rate / 12) - (payment + bonus_payment)
        total_paid = total_paid + payment + bonus_payment
        bonus_duration -= 1
    else:
        principal = principal * (1 + rate / 12) - (payment)
        total_paid = total_paid + payment
print("Total paid", total_paid)
