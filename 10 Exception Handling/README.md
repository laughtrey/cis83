# Exception Handling
Write a class Rational that will store 2 members numerator and denominator.  A rational number is defined as a number of the form a/b where a and b are integers.  
b cannot be 0.  The class should be constructed with with 2 integers as parameters.  The rational number 2/3 would be constructed using the following

number1 = Rational(2,3)



The class at construction ( __init__(self) ) . should throw an exception if the denominator is 0

use the try: except: block to output an error message.  In the __init__ member raise the error using the ValueError object.  
Test this by trying to create a Rational number with a 0 as the denominator.  
