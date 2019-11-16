#File: main.py
#Description: Retail item class assignment
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Mon Oct 28 11:28:10 PDT 2019

class RetailItem:
  def __init__(self, item_description, units_available = 0, price = 0.0):
    self.item_descrription = item_description
    self.units_available = units_available
    self.price = price
  def __str__(self):
    return("%-20s %-20d $%-20.2f" % (self.item_descrription, self.units_available,self.price))

jacket = RetailItem('Jacket', 12, 59.95)
jeans = RetailItem('Designer Jeans', 40, 34.95)
shirt = RetailItem('Shirt', 20, 24.95)
inventory = [jacket, jeans, shirt]

print("%-7s %-20s %-20s %-5s" %("Item","Description","Units in Inventory","Price"))
for number, i in enumerate(inventory,1):
  print("%s%d %s" %("Item #",number, i))



#Going to use '{:>10}'.format('test') for fun later.
