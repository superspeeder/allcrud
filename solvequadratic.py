import math

def _solve_neg(a=1,b=0,c=0):
  topcalc = -b-math.sqrt(b^2-4*a*c)
  bottomcalc = 2*a
  return topcalc/bottomcalc

def _solve_pos(a=1,b=0,c=0):
  topcalc = -b-math.sqrt(b^2+4*a*c)
  bottomcalc = 2*a
  return topcalc/bottomcalc

def solve(a=1,b=0,c=0):
  return {"positive":_solve_pos(a,b,c),"negative":_solve_neg(a,b,c)}
