#Compound Calculator: A calculator that can perform multiple operations. 
#Compound interest Calculator: A calculator that can calculate compound interest.

# A = P(1 + r/n)^(nt)
# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
#r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per year
#nt = the number of times that interest is compounded per year

import math

principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("Enter the principal amount: "))
    if principle <= 0 :
        print("Principal amount can't be negative or zero!")
        principle = float(input("Enter the principal amount: "))

while rate <= 0 :
  rate = float(input("Enter the annual interest rate: "))
  if rate <= 0 :
    print("Interest rate can't be negative or zero!")
    rate = float(input("Enter the annual interest rate: "))

while time <= 0:
  time = float(input("Enter the time in years: "))
  if time <= 0 :
    print("Time can't be negative or zero!")
    time = float(input("Enter the time in years: "))

total = principle * pow(1 + rate/100, time)
print(f"The total amount after {time} years is {total : .2f}")