# Author : foxfromworld
# Date  : 18/11/2020
# Second attempt 

def go(dividend,divisor): # Recursively subtract the divisor
  result = dividend-divisor
  if result < 0:
    return 0
  return 1+go(result,divisor)
def division_without_operator(dividend,divisor):
  sign = 1 # Necessary to check if one of the two integers is negative
  if dividend < 0 and divisor > 0 :
    sign = -1
  if dividend > 0 and divisor < 0 :
    sign = -1
  dividend = abs(dividend)
  divisor = abs(divisor)
  return sign*(go(dividend,divisor))
print(division_without_operator(10,-6))
