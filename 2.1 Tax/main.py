# File: main.py
# Description: Unit Conversion project.
# Author: Raymond Laughrey
# Email: raymonl4963@student.vvc.edu
# Date of creation: Wed Sep 11 01:31:33 PDT 2019
amount = float(input("Enter purchase price: "))
stateSalesTax = amount * .05
countySalesTax = amount * .025
print("Purchase price: ", amount, "\n" "State tax: ", stateSalesTax, "\n" "County Sales Tax: ", countySalesTax)
print("Total tax: ", stateSalesTax + countySalesTax, "\n" "Total price: ", amount + stateSalesTax + countySalesTax)
