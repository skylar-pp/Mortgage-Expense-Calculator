
print("---=== Mortgage Calculator ===---\n")

# Get user input, loan, interest rate, and 
loan = float(input("Enter the total amount of your loan: $"))
annual_interest_rate = float(input("Enter your interest rate: %"))
years = float(input("Enter the length of your loan in years: "))

#M = P((r(1+r)^n)/((1+r)^n-1))
    # M = monthly payment
    # P = principal loan amount
    # r = monthly interest rate
    # n = total number of payments (monthly)

# processing the input
r = annual_interest_rate / 1200
n = years * 12

# Calculate monthly payment
monthly_payment = loan * ((r * (1+r)**n) / ((1+r)**n-1))
print(f"This is your monthly payment: ${monthly_payment:.2f}")

# Calculate and print principal and interest payments
interest_portion = r * loan

print(f"This is your principal payment: ${monthly_payment - interest_portion:.2f}")
print(f"This is your interest payment: ${interest_portion:.2f}")