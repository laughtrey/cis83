income = int(input("What is your income per year?: "))
if income <= 50000:
  print('Your tax rate is 1%')
  incomeTax = income * .01
  print('You owe $%d' %incomeTax)
elif income <= 75000:
  print('Your tax rate is 2%')
  incomeTax = income * .02
  print('You owe $%d' %incomeTax)
elif income <= 100000:
  print('Your tax rate is 3%')
  incomeTax = income * .03
  print('You owe $%d' %incomeTax)
elif income <= 250000:
  print('Your tax rate is 4%')
  incomeTax = income * .04
  print('You owe $%d' %incomeTax)
elif income <= 500000:
  print('Your tax rate is 5%')
  incomeTax = income * .05
  print('You owe $%d' %incomeTax)
elif income > 500000:
  print('Your tax rate is 6%')
  incomeTax = income * .06
  print('You owe $%d' %incomeTax)
