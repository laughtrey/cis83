#File: reader.py
#Description: Random Number reader and writer
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Sat Nov 23 16:02:15 PDT 2019
def read():
  file = open('randomnumbers.txt')
  lines = file.readlines() #This is a list
  numberOfLines = len(lines)
  sumOfRandomNumbers = 0
  for ln in lines:
    sumOfRandomNumbers += int(ln)
  print("%s %d" % ("The sum of your random numbers is:", sumOfRandomNumbers))
  print("%s %d %s" % ("You asked for:", numberOfLines, "random numbers"))
