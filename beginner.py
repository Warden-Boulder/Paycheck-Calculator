rate = float(input("What is your payrate? "))
ot_multiplyer = 1.5
hours = float(input("How many regular hours did you work? "))
ot_hours = float(input("How many ot hours did you work? "))
tax_low = float(input("What's your lowest tax percent? "))
tax_high = float(input("What's your highest tax percent? "))

norm_pay = (rate * hours)
ot_pay = (rate * ot_multiplyer) * ot_hours
gross = (norm_pay + ot_pay)
taxed_1 = gross - (gross * (tax_low / 100))
taxed_2 = gross - (gross * (tax_high / 100))

print(f"Your regular pay is ${norm_pay:,.2f}")
print(f"Your ot pay is ${ot_pay:,.2f}")
print(f"Your gross pay is ${gross:,.2f}")
print(f"Your net pay ranges from ${taxed_2:,.2f} to ${taxed_1:,.2f}")
