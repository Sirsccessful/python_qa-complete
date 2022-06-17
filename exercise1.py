# Exercise 1: Calculate the multiplication and sum of two numbers 
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def funct(number1, number2):
    if  number1 * number2 <= 1000:
        return( number1 * number2)
    else:
       return( number1 + number2)
#Case1:
print(funct(20,30))
#CASE 2
print(funct(40,30))