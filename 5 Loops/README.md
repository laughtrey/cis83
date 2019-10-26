### Loops
>Analyzing dice rolls is a common example in understanding probability and statistics. The following program calculates the number of times the sum of two dice (randomly rolled) is equal to six or seven.

```python
import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('6s:', num_sixes)
    print('7s:', num_sevens)
else:
    print('Invalid number of rolls. Try again.')
```

Create a different version of the program that prints a histogram in which the total number of times the dice rolls 
equals each possible value is displayed by printing a character, such as *, that number of times. 

The following provides an example:

![loopexample](https://i.imgur.com/W816Pm5.png)

Due: Monday, 30 September 2019, 6:00 AM
