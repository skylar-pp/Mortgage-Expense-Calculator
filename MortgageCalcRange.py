import math

print("---=== Mortgage Calculator With Custom Inputs ===---\n")

# Get user input, loan, interest rate, and 
loan = float(input("Enter the total amount of your loan: $"))
annual_interest_rate = float(input("Enter your interest rate: %"))
#years = float(input("Enter the length of your loan in years: "))
monthly_payments = float(input("Enter the payment you want to make per month: "))

#M = P((r(1+r)^n)/((1+r)^n-1))
    # M = monthly payment
    # P = principal loan amount
    # r = monthly interest rate
    # n = total number of payments (monthly)

# processing the input
r = annual_interest_rate / 1200
n = -math.log(1 - (loan * r) / monthly_payments) / math.log(1 + r)
years = n / 12

# Calculate monthly payment
#monthly_payment = loan * ((r * (1+r)**n) / ((1+r)**n-1))

print(f"This is the number of years it will take to pay down your loan: {years:.1f} years")

# Calculate and print principal and interest payments
interest_portion = r * loan

print(f"This is your principal payment: ${monthly_payments - interest_portion:.2f}")
print(f"This is your interest payment: ${interest_portion:.2f}")

# Printing compound of monthly payment, principal payment, interest payment over the years it will take to pay down the loan

for i in range(0,12):
    print(f"This is your monthly payment for year {i+1}: ${monthly_payments:.2f}")