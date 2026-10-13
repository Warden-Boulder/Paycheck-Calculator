import pay

rate = float(input("What is your payrate? "))
ot_mult = 1.5
hours = float(input("How many regular hours did you work? "))
ot_hrs = float(input("How many ot hours did you work? "))
tax_low = float(input("What's your lowest tax percent? "))
tax_high = float(input("What's your highest tax percent? "))

gross = pay.gross(rate,hours,ot_mult, ot_hrs)
low = pay.low(gross, tax_low)
high = pay.high(gross, tax_high)
reg = pay.reg(rate,hours)
ot= pay.ot(rate,ot_mult, ot_hrs)

values = [
  ("Normal pay", reg),
  ("OT pay", ot),
  ("Gross pay", gross),
  ("Highest net pay", low),
  ("Lowest net pay", high)
]

print("")
print("---Results---")
for name, value in values:
  if value >= 1000:
    print(f"{name} is ${value:,.2f}")

  else:
    print(f"{name} is ${value:.2f}")
