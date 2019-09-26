# File: main.py
# Description: Income Tax project.
# Author: Raymond Laughrey
# Email: raymonl4963@student.vvc.edu
# Date of creation: Tue Sep 24 01:58:40 PDT 2019

import random

num_twos = 0
num_threes = 0
num_fours = 0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights = 0
num_nines = 0
num_tens = 0
num_elevens = 0
num_twelves = 0

num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of rolls
        if roll_total == 2:
            num_twos = num_twos + 1
        if roll_total == 3:
            num_threes = num_threes + 1
        if roll_total == 4:
            num_fours = num_fours + 1
        if roll_total == 5:
            num_fives = num_fives + 1
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        if roll_total == 8:
            num_eights = num_eights + 1
        if roll_total == 9:
            num_nines = num_nines + 1
        if roll_total == 10:
            num_tens = num_tens + 1
        if roll_total == 11:
            num_elevens = num_elevens + 1
        if roll_total == 12:
            num_twelves = num_twelves + 1

        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')

    print("Twos: ", end = '')
    for i in range(num_twos):
        print("*", end = '')
    print(" ")
    print("Threes: ", end = '')
    for i in range(num_threes):
        print("*", end = '')
    print(" ")
    print("Fours: ", end = '')
    for i in range(num_fours):
        print("*", end = '')
    print(" ")
    print("Fives: ", end = '')
    for i in range(num_fives):
        print("*", end = '')
    print(" ")
    print("Sixes: ", end = '')
    for i in range(num_sixes):
        print("*", end = '')
    print(" ")
    print("Sevens: ", end = '')
    for i in range(num_sevens):
        print("*", end = '')
    print(" ")
    print("Eights: ", end = '')
    for i in range(num_eights):
        print("*", end = '')
    print(" ")
    print("Nines: ", end = '')
    for i in range(num_nines):
        print("*", end = '')
    print(" ")
    print("Tens: ", end = '')
    for i in range(num_tens):
        print("*", end = '')
    print(" ")
    print("Elevens: ", end = '')
    for i in range(num_elevens):
        print("*", end = '')
    print(" ")
    print("Twelves: ", end = '')
    for i in range(num_twelves):
        print("*", end = '')
    print(" ")

else:
    print('Invalid number of rolls. Try again.')

