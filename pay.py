def gross(rate, hours, ot_mult, ot_hrs):
  return reg(rate, hours) + ot(rate, ot_mult, ot_hrs)


def low(gross_pay, tax_low):
  return gross_pay - (gross_pay * (tax_low / 100))


def high(gross_pay, tax_high):
  return gross_pay - (gross_pay * (tax_high / 100))


def reg(rate, hours):
  return rate * hours


def ot(rate, ot_mult, ot_hrs):
  return rate * ot_mult * ot_hrs
