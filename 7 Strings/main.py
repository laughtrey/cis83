#File: main.py
#Description: Sentance capitalizer, use string functions to capitalize everything in a string
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Mon Oct 08 04:25:10 PDT 2019

def capitalize_string(input_string):
  new_string_list = input_string.split()
  new_string_list = [i.capitalize() for i in new_string_list]
  formatted_string = ' '.join(new_string_list)
  print(formatted_string)

hardcoded_string = "hello. my name is Joe.  what is your name?"
capitalize_string(hardcoded_string)

s = input("Type a string!\n")
capitalize_string(s)
