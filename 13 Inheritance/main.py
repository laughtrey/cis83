#File: main.py
#Description: Inheritence project
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Tues Nov 26 05:09:37 PDT 2019

from ProductionWorker import ProductionWorker

#name = input("Please enter employee name: ")
#number = int(input("Please enter employee number: "))
#shift = int(input("Please enter shift number, 1 or 2: "))
#rate = int(input("Please enter hourly rate: $"))

name = "Bob"
number = "1337"
shift = "1"
rate = "42.0"

w1 = ProductionWorker()
w1.set_name(name)
w1.set_number(number)
w1.set_shift_number(shift)
w1.set_hourly_rate(rate)

print("Name:", w1.get_name())
print("Employee Number:", w1.get_number())

if w1.get_shift_number() == 1:
  print("Day Shift")
elif w1.get_shift_number() == 2:
  print("Night Shift")
else:
  print("Unknown shift")

print("Hourly rate: $",w1.get_hourly_rate())
