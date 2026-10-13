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

print("---------")
print(f"Your normal pay is ${reg:,.2f}")
print(f"Your ot pay is ${ot:.2f}")
print(f"Your gross pay is ${gross:,.2f}")
print(f"Your net pay ranges from ${high:,.2f} to ${low:,.2f}")
