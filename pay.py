def gross(rate,hours,ot_mult, ot_hrs):
  return reg(rate, hours) + ot(rate,ot_mult,ot_hrs)
  
def low(gross, tax_low):
  return gross-(gross*(tax_low/100))
  
def  high(gross, tax_high):
  return gross-(gross*(tax_high/100))

def reg(rate,hours):
  return rate*hours

def ot(rate,ot_mult, ot_hrs):
  return ((rate*ot_mult)*ot_hrs)