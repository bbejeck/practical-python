# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra = 1000.0
months = 0
total_payment = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
counter = 1

while principal > 0:
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        total_payment = payment + extra
    else:
        total_payment = payment

    if principal < total_payment:
        total_payment = principal
        principal = principal - total_payment
    else:
        principal = principal * (1+rate/12) - total_payment
        total_paid = total_paid + total_payment

    months = months + 1
    print(f'{months} {total_paid:2f} {principal:2f}')

print(f'Total paid is {round(total_paid, 2)} in {months} months')
