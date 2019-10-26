#File: main.py
#Description: Rainfall List assignment
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Mon Oct 21 11:35:10 PDT 2019

#Jan = float(input("Enter Janurary's Rainfall: "))
#Feb = float(input("Enter Feburary's Rainfall: "))
#Mar = float(input("Enter March's Rainfall: "))
#Apr = input("Enter April's Rainfall: ")
#May = input("Enter May's Rainfall: ")
#Jun = input("Enter June's Rainfall: ")
#Jul = input("Enter July's Rainfall: ")
#Aug = input("Enter August's Rainfall: ")
#Sep = input("Enter September's Rainfall: ")
#Oct = input("Enter October's Rainfall: ")
#Nov = input("Enter November's Rainfall: ")
#Dec = input("Enter December's Rainfall: ")

Jan = 2
Feb = 3.5
Mar = 3.5
Apr = 5
May = 6
Jun = 3.5
Jul = 2.8
Aug = 2.0
Sep = 3.2
Oct = 3.1
Nov = 2.0
Dec = 1.0

rainfall = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
rainfall.sort()
print("%s %.02f" % ("Total Rainfall: ", sum(rainfall)))
print("%s %.02f" % ("Average Rainfall: ", sum(rainfall)/len(rainfall)))
print("%s %.02f" % ("Minimum: ", rainfall[0]))
print("%s %.02f" % ("Maximum: ", rainfall[-1]))
