#File: writer.py
#Description: Random Number reader and writer
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Sat Nov 23 16:02:15 PDT 2019
def write():
  import random
  file = open('randomnumbers.txt', 'w')
  amountOfRandomNumbers = int(input("How many random numbers do you want to write to file?\n"))
  for i in range(amountOfRandomNumbers):
    randomNumber = random.randint(1,500)
    file.write(str(randomNumber))
    file.write('\n')
  file.close()
