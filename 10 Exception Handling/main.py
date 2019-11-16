#File: main.py
#Description: Retail item class assignment
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Mon Nov 4 11:26:32 PDT 2019

class Rational:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    try:
      self.denominator = denominator
      if self.denominator == 0:
        raise ValueError('Denominator can not be 0, Invalid rational number')
        del self
    except ValueError as excpt:
      print(excpt)

  def __str__(self):
    return ("%d%s%d" % (self.numerator, "/", self.denominator))

#number1 = Rational(2,3)
#print(number1)

numeratorNum2 = int(input("Enter Numerator: "))
denominatorNum2 = int(input("Enter Denominator: "))

number2 = Rational(numeratorNum2, denominatorNum2)
print(number2)
