#File: dice.py
#Description: Dice Roll Module assignment
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Fri Nov 15 21:42:15 PDT 2019

def roll():
  import random
  rolls = [0,0,0,0,0,0]
  for i in range(10000):
    roll = random.randint(1,6)
    if roll == 1:
      rolls[0] += 1
    if roll == 2:
      rolls[1] += 1
    if roll == 3:
      rolls[2] += 1
    if roll == 4:
      rolls[3] += 1
    if roll == 5:
      rolls[4] += 1
    if roll == 6:
      rolls[5] += 1        
  for side, i in enumerate(rolls,1):
    print(side,"-",i)
